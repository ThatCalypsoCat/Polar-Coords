from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP
from random import shuffle
import numpy as np

config.pixel_height=2160
config.pixel_width=3840
config.video_dir = "./videos"

class DemoScene(MovingCameraScene, PresentationScene):
    def construct(self):
        title = Text("Polar Coordinate System", z_index=3).scale(1.5)
        self.play(Write(title))
        self.end_fragment()

        self.play(
            title.animate.scale(0.5).to_corner(UL),
        )
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=18,
            y_length=18,
        )
        self.play(Create(ax))
        self.end_fragment()

        theta = ValueTracker(0)
        r = ValueTracker(1)
        dot = always_redraw(lambda: Dot(ax.polar_to_point(r.get_value(), theta.get_value()), color=RED, z_index=4))
        coord = always_redraw(lambda: MathTex(f'({r.get_value():.2f}, {theta.get_value():.2f})').next_to(dot, UP))
        l1 = always_redraw(lambda: Line(start=ax.c2p(0, 0), end=ax.polar_to_point(r.get_value(), theta.get_value()), color=BLUE_E))
        angle = always_redraw(lambda: ArcBetweenPoints(ax.c2p(0.2, 0), ax.polar_to_point(0.2, theta.get_value()), color=YELLOW, radius=0.2 * ax.get_x_unit_size()))
        line_length = always_redraw(lambda: MathTex(f'{r.get_value():.2f}').next_to(l1.get_center(), 0.5 * UP, 0.2 * LEFT))
        angle_val = always_redraw(lambda: MathTex(f'{theta.get_value():.2f}').next_to(angle.get_center(), 0.5 * RIGHT, 0.5 * UP))
        self.play(Write(VGroup(dot, coord, l1, angle)), run_time=3)
        self.end_fragment()

        self.play(theta.animate.set_value(np.pi / 4), run_time=3)
        self.play(r.animate.set_value(2), run_time=3)
        self.play(r.animate.set_value(1.5), run_time=3)
        self.play(theta.animate.set_value(np.pi / 2), run_time=3)

        self.play(theta.animate.set_value(0), run_time=3)
        self.play(r.animate.set_value(1), run_time=2)
        self.end_fragment()

        coordinates = MathTex(r'(r,\theta)').move_to(coord.get_center())
        self.play(ReplacementTransform(coord, coordinates))
        self.end_fragment()
        self.remove(angle)
        func = MathTex(r'r = \cos(4 \theta)').to_corner(UR)
        self.play(Write(func))
        t = always_redraw(lambda: MathTex(f'\\theta = {theta.get_value():.2f}').next_to(func, DOWN))
        self.play(ReplacementTransform(coordinates, t))
        self.end_fragment()

        g = always_redraw(lambda: ParametricFunction(lambda t: ax.polar_to_point(np.cos(4 * t), t), t_range=[0, theta.get_value()], stroke_color=[PINK, RED], z_index=3))
        replacementDot = always_redraw(lambda: Dot(ax.polar_to_point(np.cos(4 * theta.get_value()), theta.get_value()), color=RED, z_index=4))
        replacementLine = always_redraw(lambda: Line(start=ax.c2p(0, 0), end=ax.polar_to_point(np.cos(4 * theta.get_value()), theta.get_value()), color=BLUE_E))
        self.add(g, replacementDot, replacementLine)
        self.remove(dot, l1)
        self.play(theta.animate.set_value(2 * np.pi), run_time=10)
        self.end_fragment()