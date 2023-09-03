from manim import *

class VisualizeSigmoid(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-7, 7], 
            y_range=[-0.5, 1.5], 
            axis_config={"color": BLUE}
        )

        # Define the sigmoid function
        sigmoid_func = lambda x: 1 / (1 + np.exp(-x))
        graph = axes.plot(sigmoid_func, color=YELLOW)
        graph_label = MathTex("S(x) = \\frac{1}{1 + e^{-x}}").next_to(graph, UP, buff=0.2)

        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(2)


#manim -pql Sigmoid.py VisualizeSigmoid
