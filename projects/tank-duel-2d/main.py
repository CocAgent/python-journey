"""Chạy: python main.py. Các màn hình dùng chung một vòng lặp Pygame."""
import math
import random
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path
import pygame
from bots import Bot, SETTINGS
from entities import W, H, FIELD, COLORS, LABELS, AMMO, STYLES, Tank, Obstacle
from maps import MAPS
from ranking import leaderboard, recent_matches, rank, record_match
from sound import init as init_sound, play as sound

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tank Duel 2D")
clock = pygame.time.Clock()
init_sound()
FONT_PATH = Path(__file__).with_name("assets") / "DejaVuSans.ttf"

@lru_cache(maxsize=16)
def font(size):
    return pygame.font.Font(str(FONT_PATH), size)

def label(message, x, y, size=24, color=(238, 241, 247), center=False):
    surface = font(size).render(unicodedata.normalize("NFC", str(message)), True, color)
    screen.blit(surface, surface.get_rect(center=(x, y)) if center else (x, y))

def base(title):
    screen.fill((23, 31, 44))
    label(title, W // 2, 35, 34, center=True)

def choice(title, options, subtitle="Esc: quay lại"):
    """Menu bàn phím; trả số thứ tự hoặc None."""
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                number = event.key - pygame.K_1
                if 0 <= number < len(options):
                    return number
        base(title)
        for i, option in enumerate(options):
            label(f"{i + 1}. {option}", W // 2, 160 + i * 65, 28, center=True)
        label(subtitle, W // 2, H - 58, 19, center=True)
        pygame.display.flip()

def input_names():
    names = ["", ""]
    current, warning = 0, ""
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_BACKSPACE:
                    names[current] = names[current][:-1]
                elif event.key == pygame.K_RETURN:
                    name = names[current].strip()
                    if not name:
                        warning = "Tên không được để trống"
                    elif current == 0:
                        current = 1; warning = ""
                    elif names[0].strip().casefold() == name.casefold():
                        warning = "Hai người phải dùng tên khác nhau"; names[1] = ""
                    else:
                        return [names[0].strip(), name]
                elif event.unicode.isprintable() and len(names[current]) < 18:
                    names[current] += event.unicode
        base("ĐẤU XẾP HẠNG")
        label("Nhập tên, Enter để xác nhận từng người:", 230, 175)
        for i, name in enumerate(names):
            label(f"Người {i+1}: {name}{'|' if current == i else ''}", 260, 250 + i * 75, 27)
        label(warning, W // 2, 445, 23, (255, 125, 105), center=True)
        label("Esc: quay lại", W // 2, 640, 20, center=True)
        pygame.display.flip()

def make_game(mode, levels, names, map_name="Đấu trường", styles=(0, 0), swap=False):
    arena = MAPS[map_name]
    starts = arena["spawns"][::-1] if swap else arena["spawns"]
    p1, p2 = (Tank(*starts[0], (75, 190, 250), names[0], STYLES[styles[0]]),
              Tank(*starts[1], (250, 110, 95), names[1], STYLES[styles[1]]))
    p2.angle = math.pi if not swap else 0
    p1.angle = math.pi if swap else 0
    obstacles = [Obstacle(*data) for data in arena["obstacles"]]
    bots = (Bot(levels[0]) if levels[0] else None, Bot(levels[1]) if levels[1] else None)
    return [p1, p2], obstacles, bots

def human(keys, index, tank):
    if index == 0:
        dx = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        dy = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        fire = keys[pygame.K_SPACE]
    else:
        dx = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        dy = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        fire = keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]
    if dx or dy:
        tank.angle = math.atan2(dy, dx)
    return pygame.Vector2(dx, dy), tank.angle, fire

def spawn_item(obstacles, tanks, items):
    for _ in range(100):
        pos = pygame.Vector2(random.randint(FIELD.left + 25, FIELD.right - 25),
                             random.randint(FIELD.top + 25, FIELD.bottom - 25))
        rect = pygame.Rect(pos.x - 15, pos.y - 15, 30, 30)
        if not any(rect.colliderect(o.rect) for o in obstacles) and all(pos.distance_to(t.pos) > 65 for t in tanks) and all(pos.distance_to(old[1]) > 42 for old in items):
            items.append((random.choice(list(COLORS)), pos))
            break

def countdown(tanks, obstacles, mode, round_number, scores):
    for number in (3, 2, 1):
        draw_match(tanks, obstacles, [], [], 0, mode, round_number, scores)
        label(str(number), W//2, H//2, 85, (255, 225, 95), center=True)
        pygame.display.flip()
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 750:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return False
    return True


def pause_game():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
        label("TẠM DỪNG", W//2, 295, 50, (255, 230, 115), center=True)
        label("P: tiếp tục    Esc: về menu", W//2, 350, 24, center=True)
        pygame.display.flip()


def one_round(mode, levels, names, map_name, styles, round_number, scores):
    tanks, obstacles, bots = make_game(mode, levels, names, map_name, styles,
                                       swap=(round_number % 2 == 0))
    if not countdown(tanks, obstacles, mode, round_number, scores):
        return None, None
    bullets, items, effects = [], [], []
    broken = {}  # vị trí thùng -> thời điểm hồi lại
    elapsed, next_item, zone_tick = 0.0, 5.0, 0.0
    while True:
        dt = min(clock.tick(60) / 1000, 0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None, None
                if event.key == pygame.K_p and not pause_game():
                    return None, None
                if event.key in (pygame.K_q, pygame.K_RSHIFT):
                    index = 0 if event.key == pygame.K_q else 1
                    if bots[index] is None:
                        tanks[index].ammo = (tanks[index].ammo + 1) % len(AMMO)
        elapsed += dt
        keys = pygame.key.get_pressed()
        for i, tank in enumerate(tanks):
            other = tanks[1-i]
            direction, angle, fire = bots[i].command(tank, other, obstacles, items, bullets, dt) if bots[i] else human(keys, i, tank)
            tank.angle = angle
            tank.move(direction, dt, obstacles, other)
            tank.tick(dt)
            if fire:
                bullet = tank.shoot()
                if bullet:
                    bullets.append(bullet)
                    sound("shot")
        for bullet in bullets:
            old_hp = tanks[1].hp if bullet.owner is tanks[0] else tanks[0].hp
            target = tanks[1] if bullet.owner is tanks[0] else tanks[0]
            bullet.update(dt, obstacles, target)
            if target.hp < old_hp:
                sound("hit")
            if bullet.blast is not None:
                effects.append([bullet.blast, .3])
                sound("boom")
        bullets = [b for b in bullets if b.alive]
        for obj in obstacles[:]:
            if obj.kind == "crate" and obj.hp <= 0:
                broken[(obj.rect.x, obj.rect.y, obj.rect.w, obj.rect.h)] = elapsed + 25
                obstacles.remove(obj)
        for coords, ready in list(broken.items()):
            rectangle = pygame.Rect(*coords)
            if elapsed >= ready and not any(rectangle.colliderect(t.rect) for t in tanks):
                obstacles.append(Obstacle("crate", *coords))
                del broken[coords]
        if elapsed >= next_item:
            spawn_item(obstacles, tanks, items)
            next_item += 7
        for tank in tanks:
            for item in items[:]:
                if tank.pos.distance_to(item[1]) < 30:
                    tank.pickup(item[0]); items.remove(item)
                    sound("item")
        # Khu vực nguy hiểm chỉ xuất hiện trong 45 giây cuối.
        if elapsed >= 135:
            zone_tick += dt
            if zone_tick >= 1:
                zone_tick -= 1
                safe = FIELD.inflate(-280, -130)
                for tank in tanks:
                    if not safe.collidepoint(tank.pos):
                        tank.hit(5)
        for effect in effects:
            effect[1] -= dt
        effects = [effect for effect in effects if effect[1] > 0]
        if tanks[0].hp <= 0 or tanks[1].hp <= 0 or elapsed >= 180:
            winner = None if tanks[0].hp == tanks[1].hp else (0 if tanks[0].hp > tanks[1].hp else 1)
            return winner, tanks
        draw_match(tanks, obstacles, bullets, items, elapsed, mode, round_number, scores, effects)


def match(mode, levels=(None, None), names=("Người 1", "Người 2"),
          map_name="Đấu trường", styles=(0, 0)):
    scores = [0, 0]
    # Tối đa ba hiệp; hòa không tính điểm hiệp. Nếu cả ba hiệp hòa, trận hòa.
    for round_number in range(1, 4):
        winner, tanks = one_round(mode, levels, names, map_name, styles, round_number, scores)
        if tanks is None:
            return
        if winner is not None:
            scores[winner] += 1
        if max(scores) >= 2 or round_number == 3:
            break
        if choice(f"HIỆP {round_number}: " + ("Hòa" if winner is None else names[winner] + " thắng"),
                  ["Chơi hiệp tiếp theo", "Về menu"]) != 0:
            return
    match_winner = None if scores[0] == scores[1] else (0 if scores[0] > scores[1] else 1)
    changes = record_match(names, match_winner) if mode == "Xếp hạng" else None
    result(match_winner, tanks, changes, scores)

def draw_match(tanks, obstacles, bullets, items, elapsed, mode, round_number=1, scores=(0,0), effects=()):
    base(f"{mode}  |  Hiệp {round_number}/3  {scores[0]}-{scores[1]}  |  {int(max(0,180-elapsed)) // 60:02d}:{int(max(0,180-elapsed)) % 60:02d}")
    pygame.draw.rect(screen, (43, 59, 60), FIELD)
    pygame.draw.rect(screen, (115, 137, 139), FIELD, 3)
    if elapsed >= 135:
        safe = FIELD.inflate(-280, -130)
        pygame.draw.rect(screen, (255, 80, 75), safe, 3)
    for o in obstacles:
        if o.kind != "bush": o.draw(screen)
    for kind, pos in items:
        pygame.draw.circle(screen, COLORS[kind], pos, 15)
        label(LABELS[kind], pos.x, pos.y, 18, (17, 25, 30), center=True)
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 235, 150), bullet.pos, 5)
    for position, remaining in effects:
        pygame.draw.circle(screen, (255, 150, 60), position, int(55 * (1 - remaining/.3)), 3)
    for tank in tanks:
        hidden = any(o.kind == "bush" and o.rect.collidepoint(tank.pos) for o in obstacles)
        tank.draw(screen, hidden)
    for o in obstacles:
        if o.kind == "bush": o.draw(screen)
    for x in (26, 680):
        pygame.draw.rect(screen, (25, 36, 43), (x, 78, 294, 89), border_radius=5)
    for i, tank in enumerate(tanks):
        x = 32 if i == 0 else 686
        label(f"{tank.name[:13]}  HP {tank.hp}/100", x, 79, 19, tank.color)
        pygame.draw.rect(screen, (30, 35, 42), (x, 105, 255, 12))
        pygame.draw.rect(screen, tank.color, (x, 105, int(255 * tank.hp / 100), 12))
        active = "  ".join(f"{LABELS[k]}:{v:.0f}s" for k,v in tank.effects.items() if v > 0)
        label(active, x, 123, 16)
        label(f"Đạn: {AMMO[tank.ammo]} | Xe: {tank.style}", x, 145, 15)
    label("P1: WASD + Space + Q đổi đạn    P2: Mũi tên + Enter + Shift phải đổi đạn", 35, 639, 16)
    label("P: tạm dừng | Esc: menu | H: máu D: sát thương G: giáp S: tốc độ", 35, 667, 16)
    pygame.display.flip()

def result(winner, tanks, changes, scores=(0,0)):
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                return
        base("KẾT QUẢ")
        label("Hòa!" if winner is None else f"{tanks[winner].name} chiến thắng!", W//2, 175, 38, center=True)
        label(f"Tỉ số hiệp: {scores[0]} - {scores[1]}", W//2, 225, 26, center=True)
        if changes:
            for i, (name, old, delta, new, tier) in enumerate(changes):
                label(f"{name}: {old}  {delta:+d}  =  {new} điểm  |  {tier}", W//2, 275+i*70, 24, center=True)
        label("Enter hoặc Esc: về menu", W//2, 560, 22, center=True)
        pygame.display.flip()

def show_ranking():
    rows = leaderboard()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        base("BẢNG XẾP HẠNG")
        label("Tên                  Trận    Thắng    Thua    Điểm    Rank", 95, 113, 21)
        for i, (name, matches, wins, losses, points) in enumerate(rows):
            label(f"{i+1:>2}. {name[:16]:<18} {matches:>4}      {wins:>4}      {losses:>4}      {points:>4}     {rank(points)}", 80, 159+i*35, 20)
        label("Esc: quay lại", W//2, 650, 20, center=True)
        pygame.display.flip()

def show_history():
    rows = recent_matches()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
        base("LỊCH SỬ ĐẤU XẾP HẠNG")
        for i, (date, a, b, winner, delta_a, delta_b) in enumerate(rows):
            text = f"{date[:16]}  {a[:12]} ({delta_a:+d})  vs  {b[:12]} ({delta_b:+d})  |  {winner or 'Hòa'}"
            label(text, 40, 105+i*43, 18)
        if not rows:
            label("Chưa có trận xếp hạng", W//2, 260, center=True)
        label("Esc: quay lại", W//2, 660, 20, center=True)
        pygame.display.flip()


def setup_match():
    chosen_map = choice("CHỌN BẢN ĐỒ", list(MAPS))
    if chosen_map is None:
        return None
    styles = []
    for number in (1, 2):
        style = choice(f"CHỌN KIỂU XE {number}", STYLES,
                       "Các kiểu xe chỉ khác hình dáng, sức mạnh như nhau")
        if style is None:
            return None
        styles.append(style)
    return list(MAPS)[chosen_map], tuple(styles)

def main():
    while True:
        selected = choice("TANK DUEL 2D", ["Luyện tập", "Đấu thường", "Đấu xếp hạng", "Máy vs Máy", "Bảng xếp hạng", "Lịch sử hạng", "Thoát"], "Bấm phím số 1-7 để chọn | Esc: thoát")
        if selected is None or selected == 6: break
        if selected == 4:
            show_ranking(); continue
        if selected == 5:
            show_history(); continue
        setup = setup_match()
        if setup is None:
            continue
        map_name, styles = setup
        if selected == 0:
            level = choice("CHỌN ĐỘ KHÓ BOT", list(SETTINGS))
            if level is not None: match("Luyện tập", (None, list(SETTINGS)[level]), ("Người 1", "Máy"), map_name, styles)
        elif selected == 1:
            match("Đấu thường", map_name=map_name, styles=styles)
        elif selected == 2:
            names = input_names()
            if names: match("Xếp hạng", names=names, map_name=map_name, styles=styles)
        elif selected == 3:
            a = choice("ĐỘ KHÓ BOT 1", list(SETTINGS))
            if a is None: continue
            b = choice("ĐỘ KHÓ BOT 2", list(SETTINGS))
            if b is not None: match("Máy vs Máy", (list(SETTINGS)[a], list(SETTINGS)[b]), ("Bot 1", "Bot 2"), map_name, styles)
    pygame.quit()

if __name__ == "__main__":
    main()
