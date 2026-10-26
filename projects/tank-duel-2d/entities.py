"""Quy tắc vật lý chung cho người và bot."""
import math
import pygame

W, H = 1000, 700
FIELD = pygame.Rect(20, 75, 960, 545)
COLORS = {"heal": (70, 220, 110), "damage": (255, 110, 75),
          "armor": (95, 180, 255), "speed": (255, 220, 70)}
LABELS = {"heal": "H", "damage": "D", "armor": "G", "speed": "S"}
AMMO = ("Thường", "Nhanh", "Nổ", "Xuyên thùng")
STYLES = ("Cổ điển", "Trinh sát", "Thiết giáp")


class Tank:
    def __init__(self, x, y, color, name, style="Cổ điển"):
        self.pos = pygame.Vector2(x, y)
        self.color, self.name = color, name
        self.hp, self.angle, self.cooldown = 100, 0.0, 0.0
        self.effects = {kind: 0.0 for kind in ("damage", "armor", "speed")}
        self.velocity = pygame.Vector2()
        self.style, self.ammo, self.flash = style, 0, 0.0

    @property
    def rect(self):
        return pygame.Rect(round(self.pos.x - 19), round(self.pos.y - 19), 38, 38)

    def move(self, direction, dt, blockers, other):
        self.velocity = pygame.Vector2(direction)
        if self.velocity.length_squared():
            self.velocity.normalize_ip()
        delta = self.velocity * (210 if self.effects["speed"] > 0 else 165) * dt
        for axis in ("x", "y"):
            setattr(self.pos, axis, getattr(self.pos, axis) + getattr(delta, axis))
            if not FIELD.contains(self.rect) or any(self.rect.colliderect(o.rect) for o in blockers if o.kind != "bush") or self.rect.colliderect(other.rect):
                setattr(self.pos, axis, getattr(self.pos, axis) - getattr(delta, axis))

    def tick(self, dt):
        self.cooldown = max(0, self.cooldown - dt)
        self.flash = max(0, self.flash - dt)
        for key in self.effects:
            self.effects[key] = max(0, self.effects[key] - dt)

    def shoot(self):
        if self.hp <= 0 or self.cooldown > 0:
            return None
        self.cooldown = 0.52 if self.ammo != 1 else 0.38
        direction = pygame.Vector2(math.cos(self.angle), math.sin(self.angle))
        return Bullet(self.pos + direction * 27, direction,
                      30 if self.effects["damage"] > 0 else 20, self, self.ammo)

    def hit(self, damage):
        self.hp = max(0, self.hp - (math.ceil(damage * 0.6) if self.effects["armor"] > 0 else damage))
        self.flash = 0.18

    def pickup(self, kind):
        if kind == "heal":
            self.hp = min(100, self.hp + 30)
        else:
            self.effects[kind] = 8.0

    def draw(self, screen, hidden=False):
        if hidden:
            return
        pygame.draw.circle(screen, (22, 25, 29), self.pos, 23)
        color = (255, 255, 255) if self.flash > 0 else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=7)
        if self.style == "Trinh sát":
            pygame.draw.polygon(screen, (25, 35, 45),
                                [(self.pos.x, self.pos.y-16), (self.pos.x+14, self.pos.y),
                                 (self.pos.x, self.pos.y+16), (self.pos.x-14, self.pos.y)])
        elif self.style == "Thiết giáp":
            pygame.draw.rect(screen, (25, 35, 45), self.rect.inflate(-13, -13), 3)
        end = self.pos + pygame.Vector2(math.cos(self.angle), math.sin(self.angle)) * 30
        pygame.draw.line(screen, (245, 245, 230), self.pos, end, 9)
        pygame.draw.circle(screen, (24, 28, 38), self.pos, 7)


class Bullet:
    def __init__(self, pos, direction, damage, owner, ammo=0):
        self.pos, self.direction = pygame.Vector2(pos), pygame.Vector2(direction)
        self.damage, self.owner, self.alive = damage, owner, True
        self.ammo, self.blast = ammo, None
        self.pierced = set()

    def update(self, dt, obstacles, target):
        # Nhảy từng bước nhỏ để viên đạn không xuyên qua tường khi FPS thấp.
        travel = self.direction * (660 if self.ammo == 1 else 470) * dt
        steps = max(1, math.ceil(travel.length() / 4))
        for _ in range(steps):
            self.pos += travel / steps
            if not FIELD.collidepoint(self.pos):
                self.alive = False
                break
            for obj in obstacles:
                if obj.kind != "bush" and obj.rect.collidepoint(self.pos):
                    if obj in self.pierced:
                        continue
                    if obj.kind == "crate":
                        obj.hp -= self.damage
                        if self.ammo == 3:
                            obj.hp -= 40
                            self.pierced.add(obj)
                            continue
                    if self.ammo == 2:
                        self.blast = self.pos.copy()
                    self.alive = False
                    break
            if not self.alive:
                break
            if target.hp > 0 and target.rect.inflate(6, 6).collidepoint(self.pos):
                target.hit(self.damage)
                if self.ammo == 2:
                    self.blast = self.pos.copy()
                self.alive = False
                break
        clear_blast = not any(o.kind != "bush" and o.rect.clipline(self.blast, target.pos)
                              for o in obstacles) if self.blast is not None else False
        if self.blast is not None and clear_blast and target.hp > 0 and target.pos.distance_to(self.blast) <= 55:
            # Xe trúng trực tiếp chỉ chịu sát thương một lần.
            if not target.rect.inflate(6, 6).collidepoint(self.blast):
                target.hit(math.ceil(self.damage * 0.6))


class Obstacle:
    def __init__(self, kind, x, y, w, h):
        self.kind, self.rect = kind, pygame.Rect(x, y, w, h)
        self.hp = 60 if kind == "crate" else None

    def draw(self, screen):
        colors = {"wall": (104, 116, 128), "crate": (151, 102, 58), "bush": (42, 123, 65)}
        pygame.draw.rect(screen, colors[self.kind], self.rect, border_radius=6)
        if self.kind == "crate":
            pygame.draw.line(screen, (91, 58, 34), self.rect.topleft, self.rect.bottomright, 3)
            pygame.draw.line(screen, (91, 58, 34), self.rect.topright, self.rect.bottomleft, 3)


def visible(a, b, obstacles):
    """Bụi cây che xe đứng bên trong; vật chắn đặc chặn tầm nhìn."""
    if any(o.kind == "bush" and o.rect.collidepoint(b.pos) and not o.rect.collidepoint(a.pos) for o in obstacles):
        return False
    line = (a.pos, b.pos)
    return not any(o.kind != "bush" and o.rect.clipline(*line) for o in obstacles)
