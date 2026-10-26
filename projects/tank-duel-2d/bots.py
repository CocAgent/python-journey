"""AI chỉ nhận thông tin có thể quan sát; tất cả dùng Tank.move/shoot."""
import math
import random
import pygame
from entities import visible, FIELD

SETTINGS = {
    "Dễ": (0.85, 0.40), "Vừa": (0.42, 0.20),
    "Khó": (0.20, 0.08), "Địa ngục": (0.07, 0.015),
}


class Bot:
    def __init__(self, level):
        self.level = level
        self.timer = 0
        self.aim = 0
        self.target = pygame.Vector2()
        self.last_seen = None
        self.stride = random.choice((-1, 1))

    def command(self, me, foe, obstacles, items, bullets, dt):
        delay, error = SETTINGS[self.level]
        sight = visible(me, foe, obstacles)
        if sight:
            self.last_seen = pygame.Vector2(foe.pos)
            if self.level in ("Khó", "Địa ngục"):
                me.ammo = 1 if me.pos.distance_to(foe.pos) > 350 else 2
        elif self.level in ("Khó", "Địa ngục"):
            me.ammo = 3 if any(o.kind == "crate" for o in obstacles) else 0
        self.timer -= dt
        if self.timer <= 0:
            self.timer = delay
            goal = None
            if self.level != "Dễ" and items:
                available = [it for it in items if not (it[0] == "heal" and me.hp > (55 if self.level in ("Khó", "Địa ngục") else 75))]
                if available:
                    nearby = min(available, key=lambda it: me.pos.distance_to(it[1]))
                    if me.pos.distance_to(nearby[1]) < (420 if me.hp < 50 else 200):
                        goal = nearby[1]
            if goal is None:
                goal = foe.pos if sight else self.last_seen
            if goal is None:
                goal = FIELD.center
            self.target = pygame.Vector2(goal)
            if sight:
                aim_at = pygame.Vector2(foe.pos)
                if self.level == "Địa ngục":
                    # Dự báo chỉ từ vận tốc quan sát được khi đối thủ hiện ra.
                    flight = min(0.8, me.pos.distance_to(foe.pos) / 470)
                    aim_at += foe.velocity * 165 * flight
                vector = aim_at - me.pos
                self.aim = math.atan2(vector.y, vector.x) + random.uniform(-error, error)
        to_goal = self.target - me.pos
        direction = pygame.Vector2()
        if to_goal.length_squared() > 80 ** 2:
            direction = to_goal.normalize()
        elif sight and self.level != "Dễ" and to_goal.length_squared() > 5:
            direction = -to_goal.normalize()
        if sight and self.level in ("Vừa", "Khó", "Địa ngục"):
            diff = foe.pos - me.pos
            if diff.length_squared():
                side = pygame.Vector2(-diff.y, diff.x).normalize() * self.stride
                direction += side * (0.5 if self.level == "Vừa" else 0.9)
        if self.level != "Dễ":
            for bullet in bullets:
                if bullet.owner is foe and me.pos.distance_to(bullet.pos) < (115 if self.level == "Vừa" else 185):
                    future = bullet.pos + bullet.direction * 80
                    if me.pos.distance_to(future) < 90:
                        direction += pygame.Vector2(-bullet.direction.y, bullet.direction.x) * 2 * self.stride
        if self.level == "Địa ngục":
            # Thử các hướng vòng khi đường thẳng đến mục tiêu bị chặn.
            probe = me.pos + direction * 65
            if any(o.kind != "bush" and o.rect.inflate(38, 38).collidepoint(probe) for o in obstacles):
                direction = pygame.Vector2(-direction.y, direction.x) * self.stride
        # Chỉ bắn khi đang thấy mục tiêu, có đường đạn sạch và hướng nòng đủ gần.
        angle = math.atan2(foe.pos.y - me.pos.y, foe.pos.x - me.pos.x)
        accuracy = abs(math.atan2(math.sin(self.aim - angle), math.cos(self.aim - angle)))
        shoot = sight and accuracy < (0.30 if self.level == "Dễ" else 0.18)
        return direction, self.aim, shoot
