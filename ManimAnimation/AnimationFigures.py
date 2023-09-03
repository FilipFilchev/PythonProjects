from manim import *

class MorphShapes(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.6)

        square = Square()
        square.rotate(PI / 4)
        square.set_fill(ORANGE, opacity=0.6)

        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=0.6)

        # Adding vertex labels for triangle
        A, B, C = triangle.get_vertices()
        A_label = Tex("A").next_to(A, LEFT)
        B_label = Tex("B").next_to(B, DOWN)
        C_label = Tex("C").next_to(C, RIGHT)

        self.play(FadeIn(circle))
        self.wait(1)
        self.play(Transform(circle, square))
        self.wait(1)
        self.play(Transform(circle, triangle))
        self.play(FadeIn(A_label), FadeIn(B_label), FadeIn(C_label))
        self.wait(1)
        self.play(FadeOut(circle), FadeOut(A_label), FadeOut(B_label), FadeOut(C_label))

#manim -pql AnimationFigures.py MorphShapes
