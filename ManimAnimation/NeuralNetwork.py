from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Define a glow effect for nodes
        def glowing_dot(color):
            return Dot().set_color(color=color).set_stroke(width=8.0, color=WHITE).add_background_rectangle(opacity=0.2)

        # Define layers with colors
        input_color = BLUE
        hidden_color1 = GREEN
        hidden_color2 = PURPLE
        output_color = ORANGE

        input_layer = VGroup(*[glowing_dot(input_color) for _ in range(3)])
        input_layer.arrange(DOWN, buff=1)

        hidden_layer1 = VGroup(*[glowing_dot(hidden_color1) for _ in range(4)])
        hidden_layer1.arrange(DOWN, buff=1)

        hidden_layer2 = VGroup(*[glowing_dot(hidden_color2) for _ in range(3)])
        hidden_layer2.arrange(DOWN, buff=1)

        output_layer = VGroup(*[glowing_dot(output_color) for _ in range(2)])
        output_layer.arrange(DOWN, buff=1)

        # Positioning layers
        input_layer.move_to(LEFT*3)
        hidden_layer1.move_to(LEFT)
        hidden_layer2.move_to(RIGHT)
        output_layer.move_to(RIGHT*3)

        # Connect layers with lines
        layers = [input_layer, hidden_layer1, hidden_layer2, output_layer]
        for i in range(len(layers)-1):
            layer1 = layers[i]
            layer2 = layers[i+1]
            lines = [Line(dot1.get_center(), dot2.get_center()).set_stroke(width=1.5, color=GRAY) for dot1 in layer1 for dot2 in layer2]
            self.play(*[Create(line) for line in lines], run_time=1)

        # Display nodes
        for layer in layers:
            self.play(*[FadeIn(dot, shift=UP) for dot in layer], run_time=2)

        # Emphasize the flow of data
        arrows = [
            Arrow(LEFT*4.5, LEFT*1.5, buff=0.5, color=RED),
            Arrow(LEFT*0.5, RIGHT*0.5, buff=0.5, color=RED),
            Arrow(RIGHT*1.5, RIGHT*4.5, buff=0.5, color=RED)
        ]
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=1.5)

        self.wait(2)


#manim -pql NeuralNetwork.py NeuralNetwork
