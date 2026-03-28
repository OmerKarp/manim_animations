import os
os.environ.setdefault("TEXMFDIST", "/opt/homebrew/Cellar/texlive/20260301/share/texmf-dist")

from manim import *


BG_COLOR = "#0B1020"
ACCENT_BLUE = "#4CC9F0"
ACCENT_GREEN = "#80ED99"
ACCENT_ORANGE = "#FF9F1C"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT = "#CBD5E1"

DRAFT_MODE = os.environ.get("MANIM_DRAFT", "0") == "1"
P9_SURFACE_RESOLUTION = (16, 16) if DRAFT_MODE else (40, 40)
P9_HEADER_TIME = 1.5 if DRAFT_MODE else 2.2
P9_EQUATION_DRAW_TIME = 1.8 if DRAFT_MODE else 2.6
P9_EQUATION_GROUP_TIME = 4.2 if DRAFT_MODE else 5.8
P9_SURFACE_CREATE_TIME = 2.2 if DRAFT_MODE else 4.0
P9_SPIRAL_DRAW_TIME = 2.9 if DRAFT_MODE else 4.8
P9_EQUATION_WAIT = 1.0 if DRAFT_MODE else 2.0
P9_TRANSITION_TIME = 1.1 if DRAFT_MODE else 1.6
P9_TRANSITION_WAIT = 1.0 if DRAFT_MODE else 1.8
P9_PRE_ROTATION_WAIT = 0.8 if DRAFT_MODE else 1.4
P9_ROTATION_WAIT = 2.8 if DRAFT_MODE else 5.5
P9_POST_CAPTION_WAIT = 2.4 if DRAFT_MODE else 4.8
P9_CAMERA_RESET_TIME = 1.0 if DRAFT_MODE else 1.6
P9_FADE_TIME = 1.0 if DRAFT_MODE else 1.4
P9_AXIS_CREATE_TIME = 1.5 if DRAFT_MODE else 2.0
P9_CAPTION_TIME = 1.0 if DRAFT_MODE else 1.3


class HowToDoAPresentation(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        self.play_intro()
        self.play_break(1, "Clarity Beats Complexity")
        self.play_principle_one()
        self.play_break(2, "The Power of Colors")
        self.play_principle_two()
        self.play_break(3, "One Thing at a Time")
        self.play_principle_three()
        self.play_break(4, "It's OK to Lie (a bit)")
        self.play_principle_four()
        self.play_break(5, "Remove the Junk")
        self.play_principle_five()
        self.play_break(6, "Consistency, Consistency, Consistency")
        self.play_principle_six()
        self.play_break(7, "How to Handle Questions")
        self.play_principle_seven()
        self.play_break(8, "Not Everything Gets Equal Screentime")
        self.play_principle_eight()
        self.play_break(9, "Use Animations!")
        self.play_principle_nine()
        self.play_break(10, "Avoid Long Logical Sentences")
        self.play_principle_ten()
        self.play_break(11, "Professional Presence Is Mandatory")
        self.play_principle_eleven()
        self.play_closing()

    def build_lightbulb(self, color: str = "#FDE047"):
        bulb = Circle(radius=0.16)
        bulb.set_stroke(color=color, width=2.5)
        bulb.set_fill(color=color, opacity=0.18)

        base = RoundedRectangle(corner_radius=0.03, width=0.12, height=0.1)
        base.set_stroke(color=color, width=2)
        base.set_fill(opacity=0)
        base.next_to(bulb, DOWN, buff=0.02)

        filament_left = Line(bulb.get_center() + LEFT * 0.04, bulb.get_center() + DOWN * 0.05, color=color, stroke_width=2)
        filament_right = Line(bulb.get_center() + RIGHT * 0.04, bulb.get_center() + DOWN * 0.05, color=color, stroke_width=2)

        rays = VGroup(
            Line(bulb.get_top() + UP * 0.02, bulb.get_top() + UP * 0.12, color=color, stroke_width=2),
            Line(bulb.get_top() + LEFT * 0.1, bulb.get_top() + LEFT * 0.18 + UP * 0.08, color=color, stroke_width=2),
            Line(bulb.get_top() + RIGHT * 0.1, bulb.get_top() + RIGHT * 0.18 + UP * 0.08, color=color, stroke_width=2),
        )

        return VGroup(bulb, base, filament_left, filament_right, rays)

    def play_intro(self):
        title = Text(
            "How to Do a Presentation",
            color=TEXT_COLOR,
            weight=BOLD,
            font_size=58,
        )
        title.to_edge(UP, buff=1.0)

        equation = MathTex(
            r"x_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            color=MUTED_TEXT,
        ).scale(0.72)
        equation_box = RoundedRectangle(corner_radius=0.16, width=4.2, height=2.7)
        equation_box.set_stroke(color=ACCENT_ORANGE, width=2)
        equation_box.set_fill(opacity=0)
        equation_group = VGroup(equation_box, equation)

        esint_template = TexTemplate()
        esint_template.add_to_preamble(r"\usepackage{esint}")
        maxwell_eq = MathTex(
            r"\oiint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\mathrm{enc}}}{\epsilon_0}",
            color=MUTED_TEXT,
            tex_template=esint_template,
        ).scale(0.72)
        maxwell_box = RoundedRectangle(corner_radius=0.16, width=4.2, height=2.7)
        maxwell_box.set_stroke(color=ACCENT_GREEN, width=2)
        maxwell_box.set_fill(opacity=0)
        maxwell_group = VGroup(maxwell_box, maxwell_eq)

        code_line1 = Text("def hi():", color=ACCENT_BLUE, font_size=20, font="Courier New")
        code_line2 = Text('print("Hello world!")', color=TEXT_COLOR, font_size=20, font="Courier New")
        code_content = VGroup(code_line1, code_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        code_line2.shift(RIGHT * 0.42)
        code_box = RoundedRectangle(corner_radius=0.16, width=4.2, height=2.7)
        code_box.set_stroke(color=ACCENT_BLUE, width=2)
        code_box.set_fill(opacity=0)
        code_content.move_to(code_box.get_center())
        code_group = VGroup(code_box, code_content)

        middle_row = VGroup(equation_group, maxwell_group, code_group).arrange(RIGHT, buff=0.45)
        middle_row.move_to(DOWN * 0.15)

        subtitle = Text(
            "Knowing a topic is not the same as teaching it well.",
            color=ACCENT_BLUE,
            font_size=33,
        )
        subtitle.next_to(middle_row, DOWN, buff=0.9)

        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.0)
        self.play(Create(equation_box), Write(equation), run_time=1.0)
        self.play(Create(maxwell_box), Write(maxwell_eq), run_time=1.0)
        self.play(Create(code_box), FadeIn(code_content, shift=UP * 0.1), run_time=0.9)
        self.play(Write(subtitle), run_time=1.2)
        self.wait(2.0)
        self.play(FadeOut(title), FadeOut(middle_row), FadeOut(subtitle), run_time=0.8)

    def play_break(self, number: int, title: str):
        card = RoundedRectangle(corner_radius=0.3, width=9.5, height=5.0)
        card.set_stroke(color=ACCENT_BLUE, width=2.5)
        card.set_fill(color="#111827", opacity=0.85)
        card.move_to(ORIGIN)

        circle = Circle(radius=0.7)
        circle.set_stroke(color=ACCENT_ORANGE, width=3)
        circle.set_fill(opacity=0)
        num_text = Text(str(number), color=ACCENT_ORANGE, font_size=52, weight=BOLD)
        num_group = VGroup(circle, num_text)

        title_text = Text(title, color=TEXT_COLOR, font_size=52, weight=BOLD)

        content = VGroup(num_group, title_text).arrange(DOWN, buff=0.65)
        content.move_to(card.get_center())

        self.play(Create(card), run_time=0.6)
        self.play(Create(circle), FadeIn(num_text), run_time=0.6)
        self.play(Write(title_text), run_time=0.9)
        self.wait(2.0)
        self.play(FadeOut(card), FadeOut(content), run_time=0.7)

    def play_principle_one(self):
        header = Text("Principle 1: Clarity beats complexity", color=TEXT_COLOR, font_size=44)
        header.to_edge(UP, buff=0.55)

        teacher_body = RoundedRectangle(width=1.9, height=2.25, corner_radius=0.25)
        teacher_body.set_stroke(color="#9CA3AF", width=3)
        teacher_body.set_fill(color="#374151", opacity=0.75)
        teacher_head = Circle(radius=0.36, color="#9CA3AF", fill_opacity=1)
        teacher_head.next_to(teacher_body, UP, buff=0.12)
        teacher_eye_l = Circle(radius=0.07, color=WHITE, fill_opacity=1, stroke_width=1)
        teacher_eye_r = Circle(radius=0.07, color=WHITE, fill_opacity=1, stroke_width=1)
        teacher_eye_l.move_to(teacher_head.get_center() + LEFT * 0.11 + UP * 0.03)
        teacher_eye_r.move_to(teacher_head.get_center() + RIGHT * 0.11 + UP * 0.03)
        teacher_pupil_l = Dot(teacher_eye_l.get_center() + LEFT * 0.022 + DOWN * 0.006, radius=0.02, color=BLACK)
        teacher_pupil_r = Dot(teacher_eye_r.get_center() + LEFT * 0.022 + DOWN * 0.006, radius=0.02, color=BLACK)
        teacher_mouth_sad = ArcBetweenPoints(
            teacher_head.get_center() + LEFT * 0.09 + DOWN * 0.11,
            teacher_head.get_center() + RIGHT * 0.09 + DOWN * 0.11,
            angle=-PI / 2,
            color=BLACK,
            stroke_width=2.5,
        )
        teacher_mouth_happy = ArcBetweenPoints(
            teacher_head.get_center() + LEFT * 0.09 + DOWN * 0.11,
            teacher_head.get_center() + RIGHT * 0.09 + DOWN * 0.11,
            angle=PI / 2,
            color=BLACK,
            stroke_width=2.5,
        )
        teacher_label = Text("Teacher", color=TEXT_COLOR, font_size=24, weight=BOLD)
        teacher_label.move_to(teacher_body.get_center() + DOWN * 0.56)
        teacher = VGroup(
            teacher_body,
            teacher_head,
            teacher_eye_l,
            teacher_eye_r,
            teacher_pupil_l,
            teacher_pupil_r,
            teacher_mouth_sad,
            teacher_label,
        ).move_to(RIGHT * 3.6 + DOWN * 1.38)
        teacher_mouth_happy.move_to(teacher_mouth_sad)

        student_colors = ["#38BDF8", "#0EA5E9", "#67E8F9"]
        student_positions = [LEFT * 3.9 + DOWN * 1.66, LEFT * 2.35 + DOWN * 1.7, LEFT * 0.8 + DOWN * 1.66]
        students_confused = VGroup()
        question_marks = VGroup()
        bulbs = VGroup()
        student_mouths_sad = VGroup()
        student_mouths_happy = VGroup()
        student_checks = VGroup()

        for color, position in zip(student_colors, student_positions):
            person_head = Circle(radius=0.34, color=color, fill_opacity=1)
            person_body = RoundedRectangle(width=1.35, height=1.6, corner_radius=0.2)
            person_body.set_stroke(color=color, width=3)
            person_body.set_fill(color="#082F49", opacity=0.8)
            person_body.next_to(person_head, DOWN, buff=0.08)
            student_label = Text("Student", color=TEXT_COLOR, font_size=20, weight=BOLD)
            student_label.move_to(person_body.get_center() + DOWN * 0.43)
            look_vec = teacher.get_center() - person_head.get_center()
            look_vec = look_vec / np.linalg.norm(look_vec[:2])
            eye_l = Circle(radius=0.062, color=WHITE, fill_opacity=1, stroke_width=1)
            eye_r = Circle(radius=0.062, color=WHITE, fill_opacity=1, stroke_width=1)
            eye_l.move_to(person_head.get_center() + LEFT * 0.1 + UP * 0.02)
            eye_r.move_to(person_head.get_center() + RIGHT * 0.1 + UP * 0.02)
            pupil_shift = RIGHT * (0.02 * look_vec[0]) + UP * (0.02 * look_vec[1])
            pupil_l = Dot(eye_l.get_center() + pupil_shift, radius=0.018, color=BLACK)
            pupil_r = Dot(eye_r.get_center() + pupil_shift, radius=0.018, color=BLACK)
            mouth_sad = ArcBetweenPoints(
                person_head.get_center() + LEFT * 0.08 + DOWN * 0.1,
                person_head.get_center() + RIGHT * 0.08 + DOWN * 0.1,
                angle=-PI / 2,
                color=BLACK,
                stroke_width=2.2,
            )
            mouth_happy = ArcBetweenPoints(
                person_head.get_center() + LEFT * 0.08 + DOWN * 0.1,
                person_head.get_center() + RIGHT * 0.08 + DOWN * 0.1,
                angle=PI / 2,
                color=BLACK,
                stroke_width=2.2,
            )
            confused = VGroup(person_head, person_body, eye_l, eye_r, pupil_l, pupil_r, mouth_sad, student_label).move_to(position)
            mouth_happy.move_to(mouth_sad)
            students_confused.add(confused)

            check = Text("✓", color=ACCENT_GREEN, font_size=36, weight=BOLD)
            check.move_to(person_body.get_center())

            student_mouths_sad.add(mouth_sad)
            student_mouths_happy.add(mouth_happy)
            student_checks.add(check)

            mark = Text("?", color=TEXT_COLOR, font_size=42, weight=BOLD)
            mark.next_to(confused, UP, buff=0.2)
            question_marks.add(mark)

            bulb = self.build_lightbulb()
            bulb.scale(1.1)
            bulb.move_to(mark.get_center() + UP * 0.02)
            bulbs.add(bulb)

        complex_eq = MathTex(
            r"e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!},\ \forall x \in \mathbb{R}",
            color=MUTED_TEXT,
        ).scale(0.72)
        complex_eq.next_to(teacher, UP, buff=0.72)
        complex_eq.shift(LEFT * 0.1 + DOWN * 0.7)

        simple_eq = MathTex(
            r"e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots",
            color=ACCENT_GREEN,
        ).scale(0.72)
        simple_eq.next_to(complex_eq, UP, buff=0.55)
        simple_eq.shift(DOWN * 0.35)
        simple_eq.align_to(complex_eq, LEFT)

        cross = VGroup(
            Line(complex_eq.get_corner(UL) + LEFT * 0.2 + UP * 0.08, complex_eq.get_corner(DR) + RIGHT * 0.2 + DOWN * 0.08, color="#EF4444", stroke_width=8),
            Line(complex_eq.get_corner(UR) + RIGHT * 0.2 + UP * 0.08, complex_eq.get_corner(DL) + LEFT * 0.2 + DOWN * 0.08, color="#EF4444", stroke_width=8),
        )

        self.play(Write(header), run_time=0.8)
        self.play(FadeIn(teacher, shift=LEFT * 0.2), FadeIn(students_confused, shift=RIGHT * 0.2), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(mark, shift=UP * 0.12) for mark in question_marks], lag_ratio=0.12), run_time=0.7)
        self.play(Write(complex_eq), run_time=1.2)
        self.wait(0.7)
        self.play(Create(cross), run_time=0.9)
        self.play(FadeIn(simple_eq, shift=UP * 0.2), run_time=0.8)
        self.play(
            Transform(teacher_mouth_sad, teacher_mouth_happy),
            *[Transform(student_mouths_sad[index], student_mouths_happy[index]) for index in range(len(student_mouths_sad))],
            *[FadeIn(student_checks[index], scale=1.05) for index in range(len(student_checks))],
            *[ReplacementTransform(question_marks[index], bulbs[index]) for index in range(len(question_marks))],
            run_time=1.0,
        )
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(teacher),
            FadeOut(students_confused),
            FadeOut(complex_eq),
            FadeOut(simple_eq),
            FadeOut(cross),
            FadeOut(student_checks),
            FadeOut(bulbs),
            run_time=0.8,
        )

    def play_principle_two(self):
        header = Text("Principle 2: The Power of Colors", color=TEXT_COLOR, font_size=44)
        header.to_edge(UP, buff=0.55)

        sub = Text(
            "Track the key symbols in a Fourier transform derivation.",
            color=ACCENT_BLUE,
            font_size=30,
        )
        sub.next_to(header, DOWN, buff=0.35)

        eq1 = MathTex(
            r"\mathcal{F}\{\cos(10x)\}(\omega) = \int_{-\infty}^{\infty} \cos(10x)e^{-i\omega x}\,dx",
            substrings_to_isolate=["x", r"\omega", "10"],
            color=MUTED_TEXT,
        ).scale(0.78)
        eq1.next_to(sub, DOWN, buff=0.58)

        eq2 = MathTex(
            r"= \frac{1}{2}\int_{-\infty}^{\infty}\left(e^{i10x}+e^{-i10x}\right)e^{-i\omega x}\,dx",
            substrings_to_isolate=["x", r"\omega", "10"],
            color=MUTED_TEXT,
        ).scale(0.8)
        eq2.next_to(eq1, DOWN, buff=0.36)

        eq3 = MathTex(
            r"= \frac{1}{2}\int_{-\infty}^{\infty}\left(e^{-i(\omega-10)x}+e^{-i(\omega+10)x}\right)\,dx",
            substrings_to_isolate=["x", r"\omega", "10"],
            color=MUTED_TEXT,
        ).scale(0.8)
        eq3.next_to(eq2, DOWN, buff=0.36)

        eq4 = MathTex(
            r"= \pi\left[\delta(\omega-10)+\delta(\omega+10)\right]",
            substrings_to_isolate=["x", r"\omega", "10"],
            color=MUTED_TEXT,
        ).scale(0.92)
        eq4.next_to(eq3, DOWN, buff=0.36)

        eq_stack = VGroup(eq1, eq2, eq3, eq4)
        eq_stack.shift(UP * 0.38)

        eq1_col = eq1.copy()
        eq2_col = eq2.copy()
        eq3_col = eq3.copy()
        eq4_col = eq4.copy()

        for eq_col in (eq1_col, eq2_col, eq3_col, eq4_col):
            eq_col.set_color(MUTED_TEXT)
            eq_col.set_color_by_tex("x", ACCENT_ORANGE)
            eq_col.set_color_by_tex(r"\omega", ACCENT_BLUE)
            eq_col.set_color_by_tex("10", ACCENT_GREEN)

        color_tip = Text(
            "Now your eyes can track x, omega, and 10 instantly!",
            color=ACCENT_GREEN,
            font_size=28,
        )
        color_tip.next_to(eq4, DOWN, buff=0.52)

        self.play(Write(header), FadeIn(sub, shift=UP * 0.2), run_time=1.0)
        self.play(Write(eq1), run_time=1.0)
        self.wait(0.6)
        self.play(Write(eq2), run_time=1.0)
        self.wait(0.6)
        self.play(Write(eq3), run_time=0.9)
        self.wait(0.5)
        self.play(Write(eq4), run_time=0.85)
        self.wait(0.5)
        self.wait(1.0)
        self.play(
            Transform(eq1, eq1_col),
            Transform(eq2, eq2_col),
            Transform(eq3, eq3_col),
            Transform(eq4, eq4_col),
            run_time=1.0,
        )
        self.play(FadeIn(color_tip, shift=UP * 0.12), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(sub),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3),
            FadeOut(eq4),
            FadeOut(color_tip),
            run_time=0.8,
        )

    def play_principle_three(self):
        # ── Header ─────────────────────────────────────────────────────────
        header = Text("Principle 3: One Thing at a Time", color=TEXT_COLOR, font_size=44)
        header.to_edge(UP, buff=0.55)

        # ── Vertical divider ────────────────────────────────────────────────
        divider = Line(UP * 2.9, DOWN * 3.8, color="#4B5563", stroke_width=4)
        divider.set_x(0)

        # ── LEFT SIDE: Mind map ─────────────────────────────────────────────
        left_center = np.array([-3.6, -0.6, 0])
        center_r = 0.7

        center_circle = Circle(radius=center_r)
        center_circle.set_stroke(color=ACCENT_GREEN, width=3)
        center_circle.set_fill(color=ACCENT_GREEN, opacity=0.12)
        center_circle.move_to(left_center)
        center_label = Text("Our\nSubject", color=ACCENT_GREEN, font_size=22, weight=BOLD)
        center_label.move_to(center_circle.get_center())
        center_node = VGroup(center_circle, center_label)

        sat_names  = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Interesting\npoint!"]
        sat_angles = [95, 22, -48, -112, 158]   # degrees
        sat_dist   = 2.15
        sat_r      = 0.60

        satellite_nodes  = VGroup()
        connecting_lines = VGroup()

        for name, ang_deg in zip(sat_names, sat_angles):
            ang = ang_deg * DEGREES
            direction = np.array([np.cos(ang), np.sin(ang), 0])
            pos = left_center + sat_dist * direction

            sc = Circle(radius=sat_r)
            sc.set_stroke(color=MUTED_TEXT, width=2)
            sc.set_fill(color="#1E293B", opacity=0.85)
            sc.move_to(pos)

            sl = Text(name, color=TEXT_COLOR, font_size=13)
            sl.move_to(pos)

            line = Line(
                left_center + direction * (center_r + 0.04),
                pos         - direction * (sat_r   + 0.04),
                color="#4B5563",
                stroke_width=1.5,
            )

            satellite_nodes.add(VGroup(sc, sl))
            connecting_lines.add(line)

        # Red crosses over each satellite node
        sat_crosses = VGroup()
        for node in satellite_nodes:
            c = node[0].get_center()
            arm = 0.33
            sat_crosses.add(VGroup(
                Line(c + np.array([-arm,  arm, 0]), c + np.array([ arm, -arm, 0]),
                     color="#EF4444", stroke_width=6),
                Line(c + np.array([ arm,  arm, 0]), c + np.array([-arm, -arm, 0]),
                     color="#EF4444", stroke_width=6),
            ))

        # Focus ring around center node
        focus_ring = Circle(radius=0.82)
        focus_ring.set_stroke(color=ACCENT_GREEN, width=5)
        focus_ring.set_fill(opacity=0)
        focus_ring.move_to(left_center)

        # ── RIGHT SIDE: Presentation card ──────────────────────────────────
        card = RoundedRectangle(corner_radius=0.25, width=5.5, height=5.8)
        card.set_stroke(color=ACCENT_BLUE, width=2)
        card.set_fill(color="#111827", opacity=0.85)
        card.move_to(np.array([3.7, -0.3, 0]))

        pres_title = Text("Presentation", color=TEXT_COLOR, font_size=34, weight=BOLD)
        pres_title.move_to(card.get_top() + DOWN * 0.6)

        underline = Line(
            pres_title.get_corner(DL) + DOWN * 0.1,
            pres_title.get_corner(DR) + DOWN * 0.1,
            color=ACCENT_BLUE,
            stroke_width=2,
        )

        pres_lines = [
            Text("•  Line 1", color=MUTED_TEXT, font_size=28),
            Text("•  Line 2", color=MUTED_TEXT, font_size=28),
            Text("•  Line 3", color=MUTED_TEXT, font_size=28),
            Text("•  Line 4", color=MUTED_TEXT, font_size=28),
            Text("•  ...", color=MUTED_TEXT, font_size=28),
        ]
        pres_lines[0].next_to(underline, DOWN, buff=0.65).align_to(pres_title, LEFT)
        for i in range(1, len(pres_lines)):
            pres_lines[i].next_to(pres_lines[i - 1], DOWN, buff=0.48).align_to(pres_lines[0], LEFT)

        # ── Animations ──────────────────────────────────────────────────────
        # 1. Header + divider
        self.play(Write(header), run_time=0.8)
        self.play(Create(divider), run_time=0.5)

        # 2. Center node
        self.play(FadeIn(center_node, scale=0.8), run_time=0.6)

        # 3. Satellites radiate out (staggered)
        self.play(
            LaggedStart(
                *[AnimationGroup(Create(line), FadeIn(node, scale=0.7))
                  for line, node in zip(connecting_lines, satellite_nodes)],
                lag_ratio=0.25,
            ),
            run_time=1.6,
        )
        self.wait(0.3)

        # 4. Red crosses over satellites
        self.play(
            LaggedStart(*[Create(cross) for cross in sat_crosses], lag_ratio=0.15),
            run_time=1.0,
        )
        self.wait(0.3)

        # 5. Fade out satellites, show focus ring around Our Subject
        self.play(
            FadeOut(satellite_nodes),
            FadeOut(connecting_lines),
            FadeOut(sat_crosses),
            Create(focus_ring),
            run_time=0.8,
        )

        # 6. Blink effect (2 pulses)
        for _ in range(2):
            self.play(focus_ring.animate.scale(1.25), run_time=0.18)
            self.play(focus_ring.animate.scale(1 / 1.25), run_time=0.18)
        self.wait(0.5)

        # 7. Card + heading + underline
        self.play(Create(card), run_time=0.5)
        self.play(Write(pres_title), Create(underline), run_time=0.7)
        self.wait(0.3)

        # 8. Lines appear one at a time
        for pline in pres_lines:
            self.play(FadeIn(pline, shift=RIGHT * 0.15), run_time=0.5)
            self.wait(0.5)

        self.wait(1.5)

        # 9. Fade out
        self.play(
            FadeOut(header),
            FadeOut(divider),
            FadeOut(center_node),
            FadeOut(focus_ring),
            FadeOut(card),
            FadeOut(pres_title),
            FadeOut(underline),
            *[FadeOut(pl) for pl in pres_lines],
            run_time=0.8,
        )

    def play_principle_four(self):
        # ── Header ──────────────────────────────────────────────────────────
        header = Text("Principle 4: It's OK to Lie (a bit)", color=TEXT_COLOR, font_size=44)
        header.to_edge(UP, buff=0.55)

        # ── Vertical divider ─────────────────────────────────────────────────
        divider = Line(UP * 2.6, DOWN * 2.0, color="#4B5563", stroke_width=3)
        divider.set_x(0)

        # ── Column labels ────────────────────────────────────────────────────
        left_col_label = Text("The Precise Truth", color="#EF4444", font_size=28, weight=BOLD)
        left_col_label.move_to(np.array([-3.5, 2.2, 0]))

        right_col_label = Text("The Useful Model", color=ACCENT_GREEN, font_size=28, weight=BOLD)
        right_col_label.move_to(np.array([3.5, 2.2, 0]))

        # ── LEFT SIDE: winding path from Concept to Understanding? ────────────
        lc_x = -3.5
        wpts = [
            np.array([lc_x,        1.4,  0]),  # start (Concept)
            np.array([lc_x - 2.4,  0.7,  0]),  # swing left
            np.array([lc_x + 2.0,  0.0,  0]),  # swing right
            np.array([lc_x - 2.3, -0.7,  0]),  # swing left
            np.array([lc_x + 1.8, -1.4,  0]),  # swing right
            np.array([lc_x,       -2.0,  0]),  # end (Understanding?)
        ]

        left_path = VMobject(color="#EF4444", stroke_width=5)
        left_path.set_points_as_corners(wpts)

        caveat_labels_data = [
            ("well, actually...",  np.array([-5.2,  1.2,  0])),
            ("but technically...", np.array([-2.2,  0.35, 0])),
            ("unless...",          np.array([-5.5, -0.42, 0])),
            ("there's also...",    np.array([-2.0, -1.1,  0])),
        ]
        caveat_texts = VGroup(*[
            Text(txt, color=MUTED_TEXT, font_size=17).move_to(pos)
            for txt, pos in caveat_labels_data
        ])

        concept_dot_l = Dot(wpts[0], color=ACCENT_ORANGE, radius=0.14)
        concept_label_l = Text("Concept", color=ACCENT_ORANGE, font_size=22, weight=BOLD)
        concept_label_l.next_to(concept_dot_l, UP, buff=0.12)

        understand_dot_l = Dot(wpts[-1], color=MUTED_TEXT, radius=0.13)
        understand_l = Text("Understanding?", color=MUTED_TEXT, font_size=22)
        understand_l.next_to(understand_dot_l, DOWN, buff=0.12)

        # ── RIGHT SIDE: clean straight arrow ─────────────────────────────────
        rc = np.array([3.5, 0.0, 0])

        concept_dot_r = Dot(rc + UP * 1.4, color=ACCENT_ORANGE, radius=0.14)
        concept_label_r = Text("Concept", color=ACCENT_ORANGE, font_size=22, weight=BOLD)
        concept_label_r.next_to(concept_dot_r, UP, buff=0.12)

        understand_dot_r = Dot(rc + DOWN * 2.0, color=ACCENT_GREEN, radius=0.14)
        understand_r = Text("Understanding!", color=ACCENT_GREEN, font_size=22, weight=BOLD)
        understand_r.next_to(understand_dot_r, DOWN, buff=0.12)

        right_arrow = Arrow(
            rc + UP * 1.25,
            rc + DOWN * 1.85,
            color=ACCENT_GREEN,
            stroke_width=7,
            buff=0,
        )

        # ── Insight text ("perfect" isolated for a subtle highlight) ───────────
        insight_pre = Text("A useful model beats a", color=ACCENT_BLUE, font_size=30)
        insight_perfect = Text("perfect", color=ACCENT_BLUE, font_size=30)
        insight_post = Text("model nobody understands.", color=ACCENT_BLUE, font_size=30)
        insight = VGroup(insight_pre, insight_perfect, insight_post).arrange(RIGHT, buff=0.10)
        insight.to_edge(DOWN, buff=0.55)

        # ── Animations ───────────────────────────────────────────────────────
        self.play(Write(header), run_time=0.8)
        self.play(Create(divider), run_time=0.4)
        self.play(
            FadeIn(left_col_label, shift=RIGHT * 0.1),
            FadeIn(right_col_label, shift=LEFT * 0.1),
            run_time=0.7,
        )
        self.play(
            FadeIn(concept_dot_l), Write(concept_label_l),
            FadeIn(concept_dot_r), Write(concept_label_r),
            run_time=0.7,
        )

        # Left: tortured winding path + caveats bubbling up
        self.play(
            Create(left_path),
            LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in caveat_texts], lag_ratio=0.25),
            run_time=3.0,
        )
        self.play(FadeIn(understand_dot_l), Write(understand_l), run_time=0.6)
        self.wait(0.6)

        # Right: clean arrow rockets straight to understanding
        self.play(GrowArrow(right_arrow), run_time=0.8)
        self.play(FadeIn(understand_dot_r, scale=1.2), Write(understand_r), run_time=0.6)
        self.wait(0.8)

        self.play(Write(insight), run_time=1.0)
        self.play(
            insight_perfect.animate.set_color("#FDE047").scale(1.08),
            run_time=0.35,
        )
        self.play(
            insight_perfect.animate.set_color(ACCENT_BLUE).scale(1 / 1.08),
            run_time=0.35,
        )
        self.wait(2.0)

        # ── Fade out ─────────────────────────────────────────────────────────
        self.play(
            FadeOut(header), FadeOut(divider),
            FadeOut(left_col_label), FadeOut(right_col_label),
            FadeOut(concept_dot_l), FadeOut(concept_label_l),
            FadeOut(concept_dot_r), FadeOut(concept_label_r),
            FadeOut(left_path), FadeOut(caveat_texts),
            FadeOut(understand_dot_l), FadeOut(understand_l),
            FadeOut(right_arrow),
            FadeOut(understand_dot_r), FadeOut(understand_r),
            FadeOut(insight_pre),
            FadeOut(insight_perfect),
            FadeOut(insight_post),
            run_time=0.8,
        )

    def play_principle_five(self):
        header = Text("Principle 5: Remove the Junk", color=TEXT_COLOR, font_size=44)
        header.to_edge(UP, buff=0.55)

        slide = RoundedRectangle(corner_radius=0.24, width=11.0, height=5.5)
        slide.set_stroke(color=ACCENT_BLUE, width=2.5)
        slide.set_fill(color="#111827", opacity=0.82)
        slide.move_to(DOWN * 0.2)

        core_title = Text("Main Idea", color=ACCENT_GREEN, font_size=38, weight=BOLD)
        core_title.move_to(slide.get_center() + UP * 0.95)

        core_line = MarkupText("One <b>clear</b> message per slide.", color=TEXT_COLOR, font_size=34)
        core_line.move_to(slide.get_center() + UP * 0.1)

        junk_items = VGroup(
            Text("Long side\nstory...", color=MUTED_TEXT, font_size=20).move_to(slide.get_center() + LEFT * 3.8 + UP * 1.95),
            Text("Integral detail:\nresult = 1/4", color=MUTED_TEXT, font_size=18).move_to(slide.get_center() + RIGHT * 3.85 + UP * 1.9),
            Text("Tiny unreadable\nfootnote", color=MUTED_TEXT, font_size=15).move_to(slide.get_center() + LEFT * 2.5 + DOWN * 2.08),
            Text("Old logo", color=MUTED_TEXT, font_size=18).move_to(slide.get_center() + RIGHT * 4.1 + DOWN * 2.0),
            Text("Extra chart\nnobody needs", color=MUTED_TEXT, font_size=18).move_to(slide.get_center() + RIGHT * 3.1 + UP * 0.75),
            Text("Random fact", color=MUTED_TEXT, font_size=18).move_to(slide.get_center() + LEFT * 3.65 + DOWN * 0.55),
        )

        warning = Text(
            "If it does not help the point, cut it.",
            color=ACCENT_ORANGE,
            font_size=30,
        )
        warning.to_edge(DOWN, buff=0.5)

        final_line = Text(
            "Only keep information that moves understanding forward.",
            color=ACCENT_GREEN,
            font_size=31,
        )
        final_line.to_edge(DOWN, buff=0.5)

        self.play(Write(header), run_time=0.8)
        self.play(Create(slide), run_time=0.6)
        self.play(FadeIn(core_title, shift=UP * 0.1), FadeIn(core_line, shift=UP * 0.1), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(item, shift=UP * 0.08) for item in junk_items], lag_ratio=0.12),
            run_time=1.5,
        )
        self.wait(0.4)
        self.play(FadeIn(warning, shift=UP * 0.08), run_time=0.6)
        self.wait(0.4)

        self.play(
            LaggedStart(*[FadeOut(item, scale=0.7) for item in junk_items], lag_ratio=0.1),
            run_time=1.0,
        )
        self.play(FadeOut(warning), run_time=0.25)
        self.play(
            core_title.animate.set_color("#A7F3D0").scale(1.06),
            core_line.animate.set_color(ACCENT_GREEN).scale(1.05),
            run_time=0.55,
        )
        self.play(FadeIn(final_line, shift=UP * 0.08), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(header),
            FadeOut(slide),
            FadeOut(core_title),
            FadeOut(core_line),
            FadeOut(final_line),
            run_time=0.8,
        )

    def play_principle_six(self):
        header = Text("Principle 6: Consistency, Consistency, Consistency", color=TEXT_COLOR, font_size=40)
        header.to_edge(UP, buff=0.55)

        divider = Line(UP * 2.7, DOWN * 2.4, color="#4B5563", stroke_width=3)
        divider.set_x(0)

        left_title = Text("Consistent", color=ACCENT_GREEN, font_size=30, weight=BOLD)
        left_title.move_to(np.array([-3.4, 2.0, 0]))

        right_title = Text("Changing Mid-Lecture", color="#EF4444", font_size=30, weight=BOLD)
        right_title.move_to(np.array([3.4, 2.0, 0]))

        left_l1 = Text("x(t) = x0 + vt", color=TEXT_COLOR, font_size=36, t2c={"t": ACCENT_GREEN})
        left_l2 = Text("v(t) = v0 + at", color=TEXT_COLOR, font_size=36, t2c={"t": ACCENT_GREEN})
        left_l3 = Text("a(t) = dv/dt", color=TEXT_COLOR, font_size=36, t2c={"t": ACCENT_GREEN})
        left_stack = VGroup(left_l1, left_l2, left_l3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        left_stack.move_to(np.array([-3.4, -0.3, 0]))

        right_a = Text("x(t) = x0 + vt", color=TEXT_COLOR, font_size=36, t2c={"t": ACCENT_GREEN})
        right_b = Text("v(τ) = v0 + aτ", color=TEXT_COLOR, font_size=36, t2c={"τ": ACCENT_ORANGE})
        right_c = Text("a(T) = dv/dT", color=TEXT_COLOR, font_size=36, t2c={"T": "#F87171"})
        right_a.move_to(np.array([3.4, -0.05, 0]))

        # Target layout for cumulative, stacked equations on the right side.
        right_stack_2 = VGroup(right_a.copy(), right_b.copy()).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        right_stack_2.move_to(np.array([3.4, -0.35, 0]))
        right_stack_3 = VGroup(right_a.copy(), right_b.copy(), right_c.copy()).arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        right_stack_3.move_to(np.array([3.4, -0.35, 0]))

        # Keep upcoming equations anchored on the right so they don't pop in at the center.
        right_b.move_to(right_stack_2[1].get_center())
        right_c.move_to(right_stack_3[2].get_center())

        bad_cross = VGroup(
            Line(np.array([1.35, 0.95, 0]), np.array([5.45, -1.05, 0]), color="#EF4444", stroke_width=8),
            Line(np.array([5.45, 0.95, 0]), np.array([1.35, -1.05, 0]), color="#EF4444", stroke_width=8),
        )

        good_note = Text("t stays green everywhere", color=ACCENT_GREEN, font_size=28)
        good_note.move_to(np.array([-3.4, -2.35, 0]))

        bad_note = Text("Same concept, 3 names... confusion!", color="#FCA5A5", font_size=27)
        bad_note.move_to(np.array([3.4, -2.35, 0]))

        summary = Text(
            "Notation, color, and terms should stay stable through the whole lecture.",
            color=ACCENT_BLUE,
            font_size=28,
        )
        summary.to_edge(DOWN, buff=0.35)

        self.play(Write(header), run_time=0.8)
        self.play(Create(divider), run_time=0.45)
        self.play(FadeIn(left_title, shift=UP * 0.1), FadeIn(right_title, shift=UP * 0.1), run_time=0.6)

        self.play(LaggedStart(*[Write(line) for line in left_stack], lag_ratio=0.25), run_time=1.3)
        self.play(FadeIn(good_note, shift=UP * 0.1), run_time=0.55)
        self.wait(0.4)

        self.play(Write(right_a), run_time=0.7)
        self.wait(0.3)
        self.play(
            right_a.animate.move_to(right_stack_2[0].get_center()),
            FadeIn(right_b, shift=UP * 0.08),
            run_time=0.75,
        )
        self.wait(0.35)
        self.play(
            right_a.animate.move_to(right_stack_3[0].get_center()),
            right_b.animate.move_to(right_stack_3[1].get_center()),
            FadeIn(right_c, shift=UP * 0.08),
            run_time=0.8,
        )
        self.wait(0.45)
        self.play(Create(bad_cross), FadeIn(bad_note, shift=UP * 0.1), run_time=0.75)
        self.wait(0.9)

        self.play(Write(summary), run_time=0.9)
        self.wait(2.8)

        self.play(
            FadeOut(header),
            FadeOut(divider),
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(left_stack),
            FadeOut(right_a),
            FadeOut(right_b),
            FadeOut(right_c),
            FadeOut(bad_cross),
            FadeOut(good_note),
            FadeOut(bad_note),
            FadeOut(summary),
            run_time=0.8,
        )

    def play_principle_seven(self):
        header = Text("Principle 7: How to Handle Questions", color=TEXT_COLOR, font_size=42)
        header.to_edge(UP, buff=0.55)

        sub = Text(
            "Answer fewer live questions than you think.",
            color=ACCENT_ORANGE,
            font_size=31,
        )
        sub.next_to(header, DOWN, buff=0.3)

        question_card = RoundedRectangle(corner_radius=0.2, width=5.6, height=4.2)
        question_card.set_stroke(color=ACCENT_BLUE, width=2.2)
        question_card.set_fill(color="#111827", opacity=0.85)
        question_card.move_to(np.array([-3.4, -0.4, 0]))

        asker = VGroup(
            Circle(radius=0.22, color="#38BDF8", fill_opacity=1),
            RoundedRectangle(width=0.5, height=0.7, corner_radius=0.08),
        )
        asker[1].set_stroke(color="#38BDF8", width=2.5)
        asker[1].set_fill(color="#0C4A6E", opacity=0.9)
        asker[1].next_to(asker[0], DOWN, buff=0.06)
        asker.move_to(question_card.get_center() + LEFT * 1.25 + DOWN * 0.35)

        bubble = RoundedRectangle(corner_radius=0.14, width=2.5, height=0.9)
        bubble.set_stroke(color=MUTED_TEXT, width=1.8)
        bubble.set_fill(color="#1E293B", opacity=0.95)
        bubble.next_to(asker, UP, buff=0.16)
        q_text = Text("Can you explain that again?", color=TEXT_COLOR, font_size=17)
        q_text.move_to(bubble.get_center())

        timer_ring = Circle(radius=0.48, color=ACCENT_ORANGE, stroke_width=5)
        timer_ring.set_fill(opacity=0)
        timer_ring.move_to(question_card.get_center() + RIGHT * 1.85 + UP * 0.35)
        timer_text = Text("90s", color=ACCENT_ORANGE, font_size=34, weight=BOLD)
        timer_text.move_to(timer_ring.get_center())
        timer_label = Text("for one answer", color=MUTED_TEXT, font_size=20)
        timer_label.next_to(timer_ring, DOWN, buff=0.16)

        audience_card = RoundedRectangle(corner_radius=0.2, width=7.0, height=4.2)
        audience_card.set_stroke(color=ACCENT_GREEN, width=2.2)
        audience_card.set_fill(color="#111827", opacity=0.85)
        audience_card.move_to(np.array([3.5, -0.4, 0]))

        audience_title = Text("Rest of the class (30+)", color=ACCENT_GREEN, font_size=24, weight=BOLD)
        audience_title.move_to(audience_card.get_top() + DOWN * 0.55)

        audience_dots = VGroup(*[
            Dot(radius=0.07, color="#A7F3D0") for _ in range(33)
        ]).arrange_in_grid(rows=3, cols=11, buff=(0.34, 0.28))
        audience_dots.move_to(audience_card.get_center() + UP * 0.08)

        continuity_full = RoundedRectangle(corner_radius=0.12, width=4.8, height=0.42)
        continuity_full.set_stroke(color=ACCENT_GREEN, width=2)
        continuity_full.set_fill(color=ACCENT_GREEN, opacity=0.35)
        continuity_full.move_to(audience_card.get_center() + DOWN * 1.05)
        continuity_label = VGroup(
            Text("Lecture", color=MUTED_TEXT, font_size=20),
            Text("continuity", color=MUTED_TEXT, font_size=20),
        ).arrange(RIGHT, buff=0.22)
        continuity_label.next_to(continuity_full, DOWN, buff=0.13)

        continuity_drop = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.42)
        continuity_drop.set_stroke(color="#EF4444", width=2)
        continuity_drop.set_fill(color="#EF4444", opacity=0.4)
        continuity_drop.move_to(continuity_full.get_left() + RIGHT * 1.1)

        red_palette = ["#FCA5A5", "#FB7185", "#F87171"]

        impact = Text(
            "Better one student stays a bit unclear\nthan 30 students lose the thread.",
            color="#FCA5A5",
            font_size=28,
        )
        impact.to_edge(DOWN, buff=0.48)

        rules_card = RoundedRectangle(corner_radius=0.2, width=12.2, height=3.1)
        rules_card.set_stroke(color=ACCENT_BLUE, width=2)
        rules_card.set_fill(color="#0F172A", opacity=0.9)
        rules_card.move_to(np.array([0, -0.65, 0]))

        rules_title = Text("Practical default", color=ACCENT_BLUE, font_size=31, weight=BOLD)
        rules_title.move_to(rules_card.get_top() + DOWN * 0.4)

        rule1 = Text("1. During explanations, collect questions; do not stop every time.", color=TEXT_COLOR, font_size=24)
        rule2 = Text("2. Answer only blockers in the moment (20-40 sec max).", color=TEXT_COLOR, font_size=24)
        rule3 = Text("3. Take a short question break at section boundaries.", color=TEXT_COLOR, font_size=24)
        rules = VGroup(rule1, rule2, rule3).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        rules.move_to(rules_card.get_center() + DOWN * 0.3)

        self.play(Write(header), FadeIn(sub, shift=UP * 0.08), run_time=0.95)
        self.play(Create(question_card), Create(audience_card), run_time=0.7)
        self.play(
            FadeIn(asker, shift=UP * 0.12),
            FadeIn(bubble, shift=UP * 0.1),
            Write(q_text),
            run_time=0.85,
        )
        self.play(
            Create(timer_ring),
            FadeIn(timer_text, scale=1.08),
            FadeIn(timer_label, shift=UP * 0.08),
            run_time=0.95,
        )
        self.wait(0.35)
        self.play(
            FadeIn(audience_title, shift=UP * 0.1),
            LaggedStart(*[FadeIn(dot, scale=0.9) for dot in audience_dots], lag_ratio=0.03),
            run_time=1.3,
        )
        self.play(Create(continuity_full), FadeIn(continuity_label, shift=UP * 0.08), run_time=0.55)
        self.wait(0.4)
        self.play(
            Transform(continuity_full, continuity_drop),
            *[
                audience_dots[i].animate.set_color(red_palette[i % len(red_palette)])
                for i in range(len(audience_dots))
            ],
            run_time=2.6,
        )
        self.wait(0.8)
        self.play(Write(impact), run_time=2.6)
        self.wait(2.2)

        self.play(
            FadeOut(question_card),
            FadeOut(audience_card),
            FadeOut(asker),
            FadeOut(bubble),
            FadeOut(q_text),
            FadeOut(timer_ring),
            FadeOut(timer_text),
            FadeOut(timer_label),
            FadeOut(audience_title),
            FadeOut(audience_dots),
            FadeOut(continuity_full),
            FadeOut(continuity_label),
            FadeOut(impact),
            FadeOut(sub),
            run_time=0.7,
        )

        self.wait(2.0)

        self.play(Create(rules_card), FadeIn(rules_title, shift=UP * 0.08), run_time=0.6)
        self.play(Write(rule1), run_time=1.3)
        self.wait(2.0)
        self.play(Write(rule2), run_time=1.3)
        self.wait(2.0)
        self.play(Write(rule3), run_time=1.3)
        self.wait(2.2)

        self.play(
            FadeOut(header),
            FadeOut(rules_card),
            FadeOut(rules_title),
            FadeOut(rules),
            run_time=0.8,
        )

    def play_principle_eight(self):
        header = Text("Principle 8: Not Everything Gets Equal Screentime", color=TEXT_COLOR, font_size=38)
        header.to_edge(UP, buff=0.55)

        subtitle = Text(
            "Give more time to what matters most.",
            color=ACCENT_ORANGE,
            font_size=30,
        )
        subtitle.next_to(header, DOWN, buff=0.28)

        divider = Line(UP * 1.6, DOWN * 2.1, color="#4B5563", stroke_width=3)
        divider.set_x(0)

        left_title = Text("Core concept", color=ACCENT_GREEN, font_size=32, weight=BOLD)
        left_title.move_to(np.array([-3.4, 1.85, 0]))

        right_title = Text("Secondary detail", color=ACCENT_BLUE, font_size=32, weight=BOLD)
        right_title.move_to(np.array([3.4, 1.85, 0]))

        left_card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.8)
        left_card.set_stroke(color=ACCENT_GREEN, width=2.4)
        left_card.set_fill(color="#0F172A", opacity=0.86)
        left_card.move_to(np.array([-3.4, -0.25, 0]))

        right_card = RoundedRectangle(corner_radius=0.2, width=5.2, height=3.8)
        right_card.set_stroke(color=ACCENT_BLUE, width=2.4)
        right_card.set_fill(color="#0F172A", opacity=0.86)
        right_card.move_to(np.array([3.4, -0.25, 0]))

        core_l1 = Text("• Explain slowly", color=TEXT_COLOR, font_size=30)
        core_l2 = Text("• Show examples", color=TEXT_COLOR, font_size=30)
        core_l3 = Text("• Check understanding", color=TEXT_COLOR, font_size=30)
        core_lines = VGroup(core_l1, core_l2, core_l3).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        core_lines.move_to(left_card.get_center() + DOWN * 0.12)

        sec_l1 = Text("• Define once", color=TEXT_COLOR, font_size=28)
        sec_l2 = Text("• Give short context", color=TEXT_COLOR, font_size=28)
        sec_lines = VGroup(sec_l1, sec_l2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        sec_lines.move_to(right_card.get_center() + UP * 0.15)

        time_label = Text("Screentime budget", color=MUTED_TEXT, font_size=24)
        time_label.to_edge(DOWN, buff=1.0)

        core_bar_bg = RoundedRectangle(corner_radius=0.07, width=3.8, height=0.22)
        core_bar_bg.set_stroke(color="#334155", width=1.5)
        core_bar_bg.set_fill(color="#1E293B", opacity=1)
        core_bar_bg.move_to(np.array([-3.4, -2.45, 0]))

        core_bar_fill = RoundedRectangle(corner_radius=0.07, width=2.66, height=0.22)
        core_bar_fill.set_stroke(color=ACCENT_GREEN, width=0)
        core_bar_fill.set_fill(color=ACCENT_GREEN, opacity=0.85)
        core_bar_fill.move_to(core_bar_bg.get_left() + RIGHT * 1.33)

        core_pct = Text("70%", color=ACCENT_GREEN, font_size=26, weight=BOLD)
        core_pct.next_to(core_bar_bg, LEFT, buff=0.22)

        sec_bar_bg = RoundedRectangle(corner_radius=0.07, width=3.8, height=0.22)
        sec_bar_bg.set_stroke(color="#334155", width=1.5)
        sec_bar_bg.set_fill(color="#1E293B", opacity=1)
        sec_bar_bg.move_to(np.array([3.4, -2.45, 0]))

        sec_bar_fill = RoundedRectangle(corner_radius=0.07, width=1.14, height=0.22)
        sec_bar_fill.set_stroke(color=ACCENT_BLUE, width=0)
        sec_bar_fill.set_fill(color=ACCENT_BLUE, opacity=0.9)
        sec_bar_fill.move_to(sec_bar_bg.get_left() + RIGHT * 0.57)

        sec_pct = Text("30%", color=ACCENT_BLUE, font_size=26, weight=BOLD)
        sec_pct.next_to(sec_bar_bg, RIGHT, buff=0.22)

        takeaway = Text(
            "The teacher decides what gets depth and what gets a short pass.",
            color=ACCENT_ORANGE,
            font_size=29,
        )
        takeaway.to_edge(DOWN, buff=0.35)

        self.play(Write(header), FadeIn(subtitle, shift=UP * 0.08), run_time=1.0)
        self.play(Create(divider), FadeIn(left_title, shift=UP * 0.08), FadeIn(right_title, shift=UP * 0.08), run_time=0.7)
        self.play(Create(left_card), Create(right_card), run_time=0.7)

        self.play(LaggedStart(Write(core_l1), Write(core_l2), Write(core_l3), lag_ratio=0.35), run_time=2.2)
        self.wait(0.8)
        self.play(LaggedStart(Write(sec_l1), Write(sec_l2), lag_ratio=0.32), run_time=1.25)
        self.wait(0.7)

        self.play(
            FadeIn(time_label, shift=UP * 0.08),
            Create(core_bar_bg),
            Create(sec_bar_bg),
            run_time=0.6,
        )
        self.play(
            GrowFromEdge(core_bar_fill, LEFT),
            FadeIn(core_pct, shift=RIGHT * 0.08),
            run_time=1.0,
        )
        self.play(
            GrowFromEdge(sec_bar_fill, LEFT),
            FadeIn(sec_pct, shift=RIGHT * 0.08),
            run_time=0.6,
        )
        self.wait(0.9)
        self.play(Write(takeaway), run_time=1.0)
        self.wait(2.2)

        self.play(
            FadeOut(header),
            FadeOut(subtitle),
            FadeOut(divider),
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(left_card),
            FadeOut(right_card),
            FadeOut(core_lines),
            FadeOut(sec_lines),
            FadeOut(time_label),
            FadeOut(core_bar_bg),
            FadeOut(core_bar_fill),
            FadeOut(core_pct),
            FadeOut(sec_bar_bg),
            FadeOut(sec_bar_fill),
            FadeOut(sec_pct),
            FadeOut(takeaway),
            run_time=0.8,
        )

    def play_principle_nine(self):
        # ── PART 1: Scary static equations ──────────────────────────────────
        header = Text("Principle 9: Use Animations", color=TEXT_COLOR, font_size=38)
        header.to_edge(UP, buff=0.55)

        subtitle = Text(
            "Motion reveals what a static slide never can.",
            color=ACCENT_ORANGE,
            font_size=28,
        )
        subtitle.next_to(header, DOWN, buff=0.28)

        eq1 = Text(
            "mx\u2033(t) + \u03bcx\u2032(t) + kx(t)  =  F\u2080 cos(\u03c9t)",
            color=TEXT_COLOR,
            font_size=32,
        )
        eq2 = Text(
            "X(s)  =  F\u2080s  /  [(s\u00b2 + \u03c9\u00b2)(ms\u00b2 + \u03bcs + k)]",
            color=MUTED_TEXT,
            font_size=26,
        )
        eq3 = Text(
            "Poles:  s = \u00b1i\u03c9 ,  s = \u2212\u03bc/2m \u00b1 i\u221a(k/m \u2212 \u03bc\u00b2/4m\u00b2)",
            color=MUTED_TEXT,
            font_size=22,
        )

        eqs = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        eqs.move_to(ORIGIN + DOWN * 0.25)

        self.play(Write(header), FadeIn(subtitle, shift=UP * 0.08), run_time=P9_HEADER_TIME)
        self.wait(0.8)
        self.play(LaggedStart(Write(eq1), Write(eq2), Write(eq3), lag_ratio=0.55), run_time=P9_EQUATION_GROUP_TIME)
        self.wait(P9_EQUATION_WAIT)

        transition = Text("Now watch what that actually looks like.", color=ACCENT_GREEN, font_size=32)
        transition.to_edge(DOWN, buff=0.55)
        self.play(Write(transition), run_time=P9_TRANSITION_TIME)
        self.wait(P9_TRANSITION_WAIT)

        self.play(
            FadeOut(header), FadeOut(subtitle),
            FadeOut(eq1), FadeOut(eq2), FadeOut(eq3),
            FadeOut(transition),
            run_time=P9_FADE_TIME,
        )

        # ── PART 2: 3D rotating surface of |X(s)| showing poles ─────────────
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 4, 1],
            x_length=6,
            y_length=6,
            z_length=3.5,
            axis_config={"include_tip": True, "color": MUTED_TEXT},
        )

        x_label = axes.get_x_axis_label(Text("Re(s)", font_size=24, color=MUTED_TEXT))
        y_label = axes.get_y_axis_label(Text("Im(s)", font_size=24, color=MUTED_TEXT))

        def mag_func(u, v):
            # |X(s)| for X(s) = 1 / ((s^2+1)(s^2+2s+2))
            # Poles at s = ±i  and  s = -1 ± i
            s = complex(u, v)
            denom = (s ** 2 + 1) * (s ** 2 + 2 * s + 2)
            d_abs = abs(denom)
            val = min(1.0 / d_abs if d_abs > 0.08 else 4.5, 4.5)
            return axes.c2p(u, v, val)

        surface = Surface(
            mag_func,
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=P9_SURFACE_RESOLUTION,
            fill_opacity=0.88,
            checkerboard_colors=False,
        )
        surface.set_color_by_gradient(BLUE_E, BLUE, TEAL, GREEN_B, YELLOW, ORANGE, RED)

        caption = Text("The poles ARE the resonances.", color=ACCENT_ORANGE, font_size=30)
        caption.to_corner(DL, buff=0.5)
        self.add_fixed_in_frame_mobjects(caption)
        caption.set_opacity(0)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=P9_AXIS_CREATE_TIME)
        self.play(Create(surface), run_time=P9_SURFACE_CREATE_TIME)
        self.wait(P9_PRE_ROTATION_WAIT)

        self.begin_ambient_camera_rotation(rate=0.18)
        self.wait(P9_ROTATION_WAIT)
        self.play(caption.animate.set_opacity(1), run_time=P9_CAPTION_TIME)
        self.wait(P9_POST_CAPTION_WAIT)
        self.stop_ambient_camera_rotation()

        # Reset to 2D view before next scene
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=P9_CAMERA_RESET_TIME)
        self.play(
            FadeOut(axes), FadeOut(surface),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(caption),
            run_time=P9_FADE_TIME,
        )

        # ── PART 3: Back to the slide, then a second plotted example ───────
        header_two = Text("Principle 9: Use Animations", color=TEXT_COLOR, font_size=38)
        header_two.to_edge(UP, buff=0.55)

        subtitle_two = Text(
            "Same point. Different field.",
            color=ACCENT_ORANGE,
            font_size=28,
        )
        subtitle_two.next_to(header_two, DOWN, buff=0.28)

        eq4 = MarkupText(
            "z = x<sup>3</sup> - 3xy<sup>2</sup>",
            color=TEXT_COLOR,
            font_size=48,
            weight=BOLD,
        )
        eq4.move_to(UP * 0.2)

        eq4_note = Text(
            "A monkey saddle from differential geometry.",
            color=MUTED_TEXT,
            font_size=24,
        )
        eq4_note.next_to(eq4, DOWN, buff=0.3)

        transition_two = Text("Now rotate the surface.", color=ACCENT_GREEN, font_size=32)
        transition_two.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(header_two, shift=UP * 0.08), FadeIn(subtitle_two, shift=UP * 0.08), run_time=P9_HEADER_TIME)
        self.play(Write(eq4), FadeIn(eq4_note, shift=UP * 0.08), run_time=P9_EQUATION_DRAW_TIME)
        self.wait(P9_EQUATION_WAIT)
        self.play(Write(transition_two), run_time=P9_TRANSITION_TIME)
        self.wait(P9_TRANSITION_WAIT)
        self.play(
            FadeOut(header_two), FadeOut(subtitle_two),
            FadeOut(eq4), FadeOut(eq4_note), FadeOut(transition_two),
            run_time=P9_FADE_TIME,
        )

        self.set_camera_orientation(phi=68 * DEGREES, theta=-70 * DEGREES)

        axes_two = ThreeDAxes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-2.4, 2.4, 1],
            z_range=[-5, 5, 2],
            x_length=5.8,
            y_length=5.8,
            z_length=4.2,
            axis_config={"include_tip": True, "color": MUTED_TEXT},
        )

        x2_label = axes_two.get_x_axis_label(Text("x", font_size=24, color=MUTED_TEXT))
        y2_label = axes_two.get_y_axis_label(Text("y", font_size=24, color=MUTED_TEXT))

        def monkey_saddle(u, v):
            z = 0.34 * (u ** 3 - 3 * u * v ** 2)
            return axes_two.c2p(u, v, z)

        surface_two = Surface(
            monkey_saddle,
            u_range=[-2.1, 2.1],
            v_range=[-2.1, 2.1],
            resolution=P9_SURFACE_RESOLUTION,
            fill_opacity=0.9,
            checkerboard_colors=False,
        )
        surface_two.set_color_by_gradient(PURPLE_E, BLUE_E, TEAL, GREEN_B, YELLOW, ORANGE)

        caption_two = Text("Animation reveals the shape immediately.", color=ACCENT_ORANGE, font_size=30)
        caption_two.to_corner(DL, buff=0.5)
        self.add_fixed_in_frame_mobjects(caption_two)
        caption_two.set_opacity(0)

        self.play(Create(axes_two), FadeIn(x2_label), FadeIn(y2_label), run_time=P9_AXIS_CREATE_TIME)
        self.play(Create(surface_two), run_time=P9_SURFACE_CREATE_TIME)
        self.wait(P9_PRE_ROTATION_WAIT)

        self.begin_ambient_camera_rotation(rate=0.22)
        self.wait(P9_ROTATION_WAIT)
        self.play(caption_two.animate.set_opacity(1), run_time=P9_CAPTION_TIME)
        self.wait(P9_POST_CAPTION_WAIT)
        self.stop_ambient_camera_rotation()

        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=P9_CAMERA_RESET_TIME)
        self.play(
            FadeOut(axes_two), FadeOut(surface_two),
            FadeOut(x2_label), FadeOut(y2_label),
            FadeOut(caption_two),
            run_time=P9_FADE_TIME,
        )

        # ── PART 4: Exponential sine/cosine spiral in time ─────────────────
        header_three = Text("Principle 9: Use Animations", color=TEXT_COLOR, font_size=38)
        header_three.to_edge(UP, buff=0.55)

        subtitle_three = Text(
            "Time-dependent motion is even worse as a static formula.",
            color=ACCENT_ORANGE,
            font_size=26,
        )
        subtitle_three.next_to(header_three, DOWN, buff=0.28)

        eq5 = MarkupText(
            "r(t) = (e<sup>-0.08t</sup> cos(4t), e<sup>-0.08t</sup> sin(4t), 0.18t)",
            color=TEXT_COLOR,
            font_size=34,
            weight=BOLD,
        )
        eq5.move_to(UP * 0.2)

        eq5_note = Text(
            "A damped spiral rising through time.",
            color=MUTED_TEXT,
            font_size=24,
        )
        eq5_note.next_to(eq5, DOWN, buff=0.28)

        transition_three = Text("Now let it move.", color=ACCENT_GREEN, font_size=32)
        transition_three.to_edge(DOWN, buff=0.55)

        self.play(FadeIn(header_three, shift=UP * 0.08), FadeIn(subtitle_three, shift=UP * 0.08), run_time=P9_HEADER_TIME)
        self.play(Write(eq5), FadeIn(eq5_note, shift=UP * 0.08), run_time=P9_EQUATION_DRAW_TIME)
        self.wait(P9_EQUATION_WAIT)
        self.play(Write(transition_three), run_time=P9_TRANSITION_TIME)
        self.wait(P9_TRANSITION_WAIT)
        self.play(
            FadeOut(header_three), FadeOut(subtitle_three),
            FadeOut(eq5), FadeOut(eq5_note), FadeOut(transition_three),
            run_time=P9_FADE_TIME,
        )

        self.set_camera_orientation(phi=72 * DEGREES, theta=-55 * DEGREES)

        axes_three = ThreeDAxes(
            x_range=[-1.4, 1.4, 0.5],
            y_range=[-1.4, 1.4, 0.5],
            z_range=[0, 5.5, 1],
            x_length=4.5,
            y_length=4.5,
            z_length=5.0,
            axis_config={"include_tip": True, "color": MUTED_TEXT},
        )

        x3_label = axes_three.get_x_axis_label(Text("x", font_size=24, color=MUTED_TEXT))
        y3_label = axes_three.get_y_axis_label(Text("y", font_size=24, color=MUTED_TEXT))
        z3_label = axes_three.get_z_axis_label(Text("t", font_size=24, color=MUTED_TEXT))

        def spiral_point(t_value):
            return axes_three.c2p(
                np.exp(-0.08 * t_value) * np.cos(4 * t_value),
                np.exp(-0.08 * t_value) * np.sin(4 * t_value),
                0.18 * t_value,
            )

        spiral = ParametricFunction(
            spiral_point,
            t_range=[0, 8 * PI],
            color=ACCENT_BLUE,
            stroke_width=5,
        )

        tracker = ValueTracker(0.0)
        moving_dot = always_redraw(
            lambda: Dot3D(point=spiral_point(tracker.get_value()), radius=0.06, color=ACCENT_ORANGE)
        )

        caption_three = Text("A single animation makes the time behavior obvious.", color=ACCENT_ORANGE, font_size=28)
        caption_three.to_corner(DL, buff=0.5)
        self.add_fixed_in_frame_mobjects(caption_three)
        caption_three.set_opacity(0)

        self.play(Create(axes_three), FadeIn(x3_label), FadeIn(y3_label), FadeIn(z3_label), run_time=P9_AXIS_CREATE_TIME)
        self.add(moving_dot)
        self.play(
            Create(spiral, rate_func=linear),
            tracker.animate.set_value(8 * PI),
            run_time=P9_SPIRAL_DRAW_TIME,
        )
        self.wait(P9_PRE_ROTATION_WAIT)

        self.begin_ambient_camera_rotation(rate=0.24)
        self.play(caption_three.animate.set_opacity(1), run_time=P9_CAPTION_TIME)
        self.wait(P9_ROTATION_WAIT)
        self.wait(P9_POST_CAPTION_WAIT)
        self.stop_ambient_camera_rotation()

        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=P9_CAMERA_RESET_TIME)
        self.play(
            FadeOut(axes_three), FadeOut(spiral), FadeOut(moving_dot),
            FadeOut(x3_label), FadeOut(y3_label), FadeOut(z3_label),
            FadeOut(caption_three),
            run_time=P9_FADE_TIME,
        )

    def play_closing(self):
        row_title = Text("11 Principles", color=TEXT_COLOR, font_size=38, weight=BOLD)
        row_title.to_edge(UP, buff=0.55)

        red_color = "#EF4444"
        circles = VGroup()
        numbers = VGroup()
        chips = []
        for i in range(1, 12):
            circle = Circle(radius=0.34)
            circle.set_stroke(color=red_color, width=3)
            circle.set_fill(color=red_color, opacity=0.12)
            num = Text(str(i), color=red_color, font_size=32, weight=BOLD)
            num.move_to(circle.get_center())
            chip = VGroup(circle, num)
            circles.add(circle)
            numbers.add(num)
            chips.append(chip)

        chips_group = VGroup(*chips).arrange(RIGHT, buff=0.18)
        chips_group.move_to(UP * 1.35)

        slider_width = 9.8
        slider_track = RoundedRectangle(corner_radius=0.14, width=slider_width, height=0.54)
        slider_track.set_stroke(color="#334155", width=2)
        slider_track.set_fill(color="#111827", opacity=0.95)
        slider_track.move_to(DOWN * 1.0)

        progress = ValueTracker(0)
        slider_fill = always_redraw(
            lambda: RoundedRectangle(
                corner_radius=0.14,
                width=max(0.25, slider_width * progress.get_value() / 11),
                height=0.54,
            )
            .set_stroke(width=0)
            .set_fill(color=ACCENT_GREEN, opacity=0.95)
            .move_to(slider_track.get_left() + RIGHT * (max(0.25, slider_width * progress.get_value() / 11) / 2))
        )

        status_colors = {
            "meh": "#F87171",
            "ok": "#F59E0B",
            "good": "#84CC16",
            "great": "#22C55E",
            "amazing!": "#4CC9F0",
        }

        status = Text("Meh", color=status_colors["meh"], font_size=38, weight=BOLD)
        status.next_to(slider_track, DOWN, buff=0.35)

        self.play(FadeIn(row_title, shift=UP * 0.08), run_time=0.6)
        self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.06), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(n, scale=0.9) for n in numbers], lag_ratio=0.06), run_time=0.9)
        self.play(Create(slider_track), FadeIn(slider_fill), FadeIn(status, shift=UP * 0.06), run_time=0.9)
        self.wait(0.3)

        reveal_order = list(np.random.permutation(11))

        for step_index, chip_index in enumerate(reveal_order, start=1):
            circle = circles[chip_index]
            num = numbers[chip_index]

            next_text = "Meh"
            next_color = status_colors["meh"]
            if step_index >= 10:
                next_text = "amazing!"
                next_color = status_colors["amazing!"]
            elif step_index >= 7:
                next_text = "great"
                next_color = status_colors["great"]
            elif step_index >= 4:
                next_text = "good"
                next_color = status_colors["good"]
            elif step_index >= 1:
                next_text = "ok"
                next_color = status_colors["ok"]

            new_status = Text(next_text, color=next_color, font_size=38, weight=BOLD)
            new_status.move_to(status)

            self.play(
                circle.animate.set_stroke(color=ACCENT_GREEN, width=3).set_fill(color=ACCENT_GREEN, opacity=0.18).scale(1.18),
                num.animate.set_color(ACCENT_GREEN).scale(1.18),
                progress.animate.set_value(step_index),
                Transform(status, new_status),
                run_time=0.38,
            )
            self.play(circle.animate.scale(1 / 1.18), num.animate.scale(1 / 1.18), run_time=0.16)

        self.wait(1.2)
        self.play(FadeOut(row_title), FadeOut(chips_group), FadeOut(slider_track), FadeOut(slider_fill), FadeOut(status), run_time=0.8)

    def play_principle_ten(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        header = Text("Principle 10: Avoid Long Logical Sentences", color=TEXT_COLOR, font_size=36)
        header.to_edge(UP, buff=0.55)

        subtitle = Text("Erase the paragraph. Teach one step at a time.", color=ACCENT_ORANGE, font_size=28)
        subtitle.next_to(header, DOWN, buff=0.25)

        overload_box = RoundedRectangle(corner_radius=0.18, width=12.2, height=3.1)
        overload_box.set_stroke(color="#7F1D1D", width=2.5)
        overload_box.set_fill(color="#1F2937", opacity=0.72)
        overload_box.move_to(DOWN * 0.5)

        overload_text = Text(
            "When f(x) goes from -3 to 9, then we take the second derivative,\n"
            "apply the Fourier transform, multiply by g(x) from 3 to 12,\n"
            "and eventually get a rectangle...",
            color="#FCA5A5",
            font_size=30,
        )
        overload_text.move_to(overload_box.get_center())

        too_much = Text("Too much at once.", color="#F87171", font_size=34, weight=BOLD)
        too_much.next_to(overload_box, DOWN, buff=0.35)

        strike_1 = Line(overload_box.get_corner(UL) + DOWN * 0.2, overload_box.get_corner(DR) + UP * 0.2, color="#EF4444", stroke_width=10)
        strike_2 = Line(overload_box.get_corner(UR) + DOWN * 0.2, overload_box.get_corner(DL) + UP * 0.2, color="#EF4444", stroke_width=10)

        self.play(Write(header), FadeIn(subtitle, shift=UP * 0.08), run_time=1.4)
        self.play(Create(overload_box), run_time=1.0)
        self.play(Write(overload_text), run_time=4.2)
        self.wait(1.2)
        self.play(Create(strike_1), Create(strike_2), FadeIn(too_much, shift=UP * 0.1), run_time=1.2)
        self.wait(1.2)
        self.play(
            FadeOut(overload_box), FadeOut(overload_text),
            FadeOut(strike_1), FadeOut(strike_2), FadeOut(too_much),
            run_time=0.9,
        )

        board = RoundedRectangle(corner_radius=0.12, width=13.8, height=7.2)
        board.set_stroke(color="#CBD5E1", width=2.2)
        board.set_fill(color="#F8FAFC", opacity=0.98)
        board.move_to(ORIGIN)

        board_title = Text("Whiteboard: one step at a time", color="#0F172A", font_size=34, weight=BOLD)
        board_title.move_to(board.get_top() + DOWN * 0.45)

        step1 = Text("1) Start with f(x)", color="#0F172A", font_size=30, weight=BOLD)
        step1.move_to(board.get_center() + np.array([-2.8, 2.35, 0]))

        axis_x = Line(board.get_center() + np.array([-3.6, 1.2, 0]), board.get_center() + np.array([-0.8, 1.2, 0]), color="#334155", stroke_width=4)
        axis_y = Line(board.get_center() + np.array([-3.2, 0.0, 0]), board.get_center() + np.array([-3.2, 1.9, 0]), color="#334155", stroke_width=4)
        f_curve = FunctionGraph(lambda x: 0.45 * np.sin(2.2 * x) + 0.1 * x, x_range=[-1.8, 1.8], color=ACCENT_BLUE, stroke_width=5)
        f_curve.move_to(board.get_center() + np.array([-2.0, 1.2, 0]))

        step2 = Text("2) Now take f''(x)", color="#0F172A", font_size=30, weight=BOLD)
        step2.move_to(board.get_center() + np.array([2.5, 2.35, 0]))
        d2_box = RoundedRectangle(corner_radius=0.12, width=3.6, height=1.1)
        d2_box.set_stroke(color=ACCENT_ORANGE, width=3)
        d2_box.set_fill(color="#FEF3C7", opacity=0.7)
        d2_box.move_to(board.get_center() + np.array([2.5, 1.2, 0]))
        d2_text = Text("f″(x) = 5x", color="#0F172A", font_size=40, weight=BOLD)
        d2_text.move_to(d2_box.get_center())

        step3 = Text("3) Then Fourier transform", color="#0F172A", font_size=30, weight=BOLD)
        step3.move_to(board.get_center() + np.array([-2.5, -0.35, 0]))
        fourier_box = RoundedRectangle(corner_radius=0.12, width=2.6, height=1.0)
        fourier_box.set_stroke(color=ACCENT_GREEN, width=3)
        fourier_box.set_fill(color="#DCFCE7", opacity=0.8)
        fourier_box.move_to(board.get_center() + np.array([-2.5, -1.4, 0]))
        fourier_text = Text("F(ω)", color="#0F172A", font_size=36, weight=BOLD)
        fourier_text.move_to(fourier_box.get_center())

        step4 = Text("4) Multiply by g(ω)", color="#0F172A", font_size=30, weight=BOLD)
        step4.move_to(board.get_center() + np.array([2.5, -0.35, 0]))
        multiply = Text("F(ω) · g(ω)", color="#0F172A", font_size=30, weight=BOLD)
        multiply.move_to(board.get_center() + np.array([2.5, -1.4, 0]))
        mul_box = RoundedRectangle(corner_radius=0.12, width=3.8, height=0.95)
        mul_box.set_stroke(color="#0EA5E9", width=3)
        mul_box.set_fill(color="#DBEAFE", opacity=0.7)
        mul_box.move_to(multiply.get_center())

        step5 = Text("5) Final shape: triangle", color="#0F172A", font_size=30, weight=BOLD)
        step5.move_to(board.get_center() + np.array([-1.9, -2.75, 0]))
        tri_result = Polygon(
            np.array([0.0, 0.65, 0.0]),
            np.array([-0.95, -0.6, 0.0]),
            np.array([0.95, -0.6, 0.0]),
            color="#FDE047",
            stroke_width=5,
        )
        tri_result.set_fill(color="#7C3AED", opacity=0.95)
        tri_result.move_to(board.get_center() + np.array([3.0, -2.75, 0]))

        self.play(Create(board), FadeIn(board_title, shift=UP * 0.08), run_time=1.3)
        self.play(Write(step1), run_time=1.0)
        self.play(Create(axis_x), Create(axis_y), Create(f_curve), run_time=1.9)
        self.wait(1.0)

        self.play(Write(step2), run_time=1.0)
        self.play(Create(d2_box), Write(d2_text), run_time=1.3)
        self.wait(1.0)

        self.play(Write(step3), run_time=1.0)
        self.play(Create(fourier_box), Write(fourier_text), run_time=1.3)
        self.wait(1.0)

        self.play(Write(step4), run_time=1.0)
        self.play(Create(mul_box), Write(multiply), run_time=1.2)
        self.wait(1.0)

        self.play(Write(step5), run_time=1.0)
        self.play(DrawBorderThenFill(tri_result), run_time=1.1)
        self.wait(1.2)
        self.wait(1.2)

        self.play(
            FadeOut(header), FadeOut(subtitle), FadeOut(board_title),
            FadeOut(board), FadeOut(step1), FadeOut(axis_x), FadeOut(axis_y), FadeOut(f_curve),
            FadeOut(step2), FadeOut(d2_box), FadeOut(d2_text),
            FadeOut(step3), FadeOut(fourier_box), FadeOut(fourier_text),
            FadeOut(step4), FadeOut(mul_box), FadeOut(multiply),
            FadeOut(step5), FadeOut(tri_result),
            run_time=1.0,
        )

    def play_principle_eleven(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        header = Text("Principle 11: Professional Presence Is Mandatory", color=TEXT_COLOR, font_size=36)
        header.to_edge(UP, buff=0.55)

        subtitle = Text(
            "Small personal mistakes can destroy credibility.",
            color=ACCENT_ORANGE,
            font_size=28,
        )
        subtitle.next_to(header, DOWN, buff=0.25)

        left_panel = RoundedRectangle(corner_radius=0.16, width=6.1, height=4.9)
        left_panel.set_stroke(color="#334155", width=2.2)
        left_panel.set_fill(color="#0F172A", opacity=0.86)
        left_panel.move_to(np.array([-3.35, -0.55, 0]))

        right_panel = RoundedRectangle(corner_radius=0.16, width=6.1, height=4.9)
        right_panel.set_stroke(color="#334155", width=2.2)
        right_panel.set_fill(color="#0F172A", opacity=0.86)
        right_panel.move_to(np.array([3.35, -0.55, 0]))

        checklist_title = Text("Before Every Lecture", color=TEXT_COLOR, font_size=30, weight=BOLD)
        checklist_title.move_to(left_panel.get_top() + DOWN * 0.5)

        item1 = Text("1) Clean hygiene", color=TEXT_COLOR, font_size=28)
        item2 = Text("2) Use deodorant", color=TEXT_COLOR, font_size=28)
        item3 = Text("3) Brush your teeth", color=TEXT_COLOR, font_size=28)
        item4 = Text("4) Review the material", color=TEXT_COLOR, font_size=28)

        items = VGroup(item1, item2, item3, item4).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        items.move_to(left_panel.get_center() + np.array([0.0, -0.40, 0]))

        x_marks = VGroup(
            Text("✖", color="#EF4444", font_size=44, weight=BOLD),
            Text("✖", color="#EF4444", font_size=44, weight=BOLD),
            Text("✖", color="#EF4444", font_size=44, weight=BOLD),
            Text("✖", color="#EF4444", font_size=44, weight=BOLD),
        )
        x_marks[0].next_to(item1, RIGHT, buff=0.3)
        x_marks[1].next_to(item2, RIGHT, buff=0.3)
        x_marks[2].next_to(item3, RIGHT, buff=0.3)
        x_marks[3].next_to(item4, RIGHT, buff=0.3)

        check_marks = VGroup(
            Text("✔", color=ACCENT_GREEN, font_size=40, weight=BOLD),
            Text("✔", color=ACCENT_GREEN, font_size=40, weight=BOLD),
            Text("✔", color=ACCENT_GREEN, font_size=40, weight=BOLD),
            Text("✔", color=ACCENT_GREEN, font_size=40, weight=BOLD),
        )
        check_marks[0].move_to(x_marks[0])
        check_marks[1].move_to(x_marks[1])
        check_marks[2].move_to(x_marks[2])
        check_marks[3].move_to(x_marks[3])

        cred_title = Text("Student Trust", color=TEXT_COLOR, font_size=30, weight=BOLD)
        cred_title.move_to(right_panel.get_top() + DOWN * 0.5)

        trust_bg = RoundedRectangle(corner_radius=0.1, width=4.6, height=0.62)
        trust_bg.set_stroke(color="#334155", width=1.5)
        trust_bg.set_fill(color="#1E293B", opacity=1)
        trust_bg.move_to(right_panel.get_center() + np.array([0.0, 0.35, 0]))

        trust_fill = RoundedRectangle(corner_radius=0.1, width=4.2, height=0.62)
        trust_fill.set_stroke(width=0)
        trust_fill.set_fill(color=ACCENT_GREEN, opacity=0.92)
        trust_fill.move_to(trust_bg.get_left() + RIGHT * 2.1)

        trust_label = Text("High", color=ACCENT_GREEN, font_size=28, weight=BOLD)
        trust_label.next_to(trust_bg, DOWN, buff=0.22)

        warning = Text(
            "If basic hygiene and preparation fail,\n"
            "students stop trusting the teacher.",
            color="#FCA5A5",
            font_size=26,
        )
        warning.move_to(right_panel.get_center() + np.array([0.0, -1.1, 0]))

        mandatory = Text("Mandatory. Not optional.", color=ACCENT_ORANGE, font_size=34, weight=BOLD)
        mandatory.to_edge(DOWN, buff=0.35)

        trust_low_fill = RoundedRectangle(corner_radius=0.1, width=1.25, height=0.62)
        trust_low_fill.set_stroke(width=0)
        trust_low_fill.set_fill(color="#F97316", opacity=0.95)
        trust_low_fill.move_to(trust_bg.get_left() + RIGHT * 0.625)

        trust_label_low = Text("Low", color="#F97316", font_size=28, weight=BOLD)
        trust_label_low.move_to(trust_label)

        self.play(Write(header), FadeIn(subtitle, shift=UP * 0.08), run_time=1.3)
        self.play(Create(left_panel), Create(right_panel), run_time=1.0)

        self.play(Write(checklist_title), Write(cred_title), run_time=1.0)
        self.play(LaggedStart(Write(item1), Write(item2), Write(item3), Write(item4), lag_ratio=0.2), run_time=2.0)

        self.play(LaggedStart(*[FadeIn(cm, shift=RIGHT * 0.08) for cm in check_marks], lag_ratio=0.18), run_time=1.2)
        self.play(Create(trust_bg), FadeIn(trust_fill), FadeIn(trust_label, shift=UP * 0.08), run_time=1.0)
        self.play(FadeIn(warning, shift=UP * 0.08), run_time=0.9)
        self.wait(1.0)

        self.play(
            ReplacementTransform(trust_fill, trust_low_fill),
            ReplacementTransform(trust_label, trust_label_low),
            Transform(check_marks[0], x_marks[0]),
            Transform(check_marks[1], x_marks[1]),
            Transform(check_marks[2], x_marks[2]),
            Transform(check_marks[3], x_marks[3]),
            run_time=1.0,
        )
        self.wait(0.9)

        self.play(Write(mandatory), run_time=1.0)
        self.wait(2.0)

        self.play(
            FadeOut(header), FadeOut(subtitle), FadeOut(left_panel), FadeOut(right_panel),
            FadeOut(checklist_title), FadeOut(cred_title),
            FadeOut(item1), FadeOut(item2), FadeOut(item3), FadeOut(item4),
            FadeOut(check_marks[0]), FadeOut(check_marks[1]), FadeOut(check_marks[2]), FadeOut(check_marks[3]),
            FadeOut(trust_bg), FadeOut(trust_low_fill), FadeOut(trust_label_low), FadeOut(warning),
            FadeOut(mandatory),
            run_time=0.9,
        )


class IntroOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_intro()


class PrincipleOneOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_one()


class PrincipleTwoOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_two()


class PrincipleThreeOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_three()


class PrincipleFourOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_four()


class PrincipleFiveOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_five()


class PrincipleSixOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_six()


class PrincipleSevenOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_seven()


class PrincipleEightOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_eight()


class PrincipleNineOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_nine()


class PrincipleTenOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_ten()


class PrincipleElevenOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_principle_eleven()


class OutroOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_closing()


class BreakOnly(HowToDoAPresentation):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.play_break(1, "Clarity Beats Complexity")
