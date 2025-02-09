from manim import *

class PartV(Scene): 
    def construct(self):
        
        # Create Text and Shapes
        text1 = Text('Adding Random Shapes')
        s1 = Dot().next_to(text1, LEFT*0.5 + DOWN*2)
        s2 = Sector(color=PINK).next_to(s1, RIGHT*4).scale(0.5)
        s3 = Circle(fill_opacity=1).next_to(s2,RIGHT).scale(0.25)
        s4 = Triangle(fill_opacity=1).next_to(s3,RIGHT).scale(0.25)
        s5 = Square(fill_opacity=1,color=ORANGE).next_to(s4,RIGHT).scale(0.25)
        s6 = Star(7, density=2, color=RED,fill_opacity=1).next_to(s5,RIGHT).scale(0.25)

        # Play animations in the correct format
        self.play(Succession(Create(text1),Circumscribe(text1)))
        self.wait()
        self.play(Succession(SpinInFromNothing(s1),GrowFromPoint(s2,s1),GrowFromPoint(s3,s2), GrowFromPoint(s4,s3),GrowFromPoint(s5,s4), GrowFromPoint(s6,s5)))

        self.wait(2)
        

        text2 = Text('Adding Shadows')
        s7 = Square(side_length=1.5,fill_opacity=1).next_to(text2,DOWN*4).set_z_index(2)
        s7_s= Square(side_length=1.5,color=GREY,fill_opacity=1)
        s7_ss= Square(side_length=1.5,color=GREY,fill_opacity=1)

        matrix = [[1, 1], [1.5, 0]]
        matrix2= [[1,1],[-1.5,0]]
        s7_s.apply_matrix(matrix).next_to(text2,DOWN).shift(RIGHT*0.7).set_z_index(1)
        s7_ss.apply_matrix(matrix2).next_to(text2,DOWN).shift(LEFT*0.7).set_z_index(1)

        self.play(Succession(Create(text2),Circumscribe(text2),Create(s7)))
        self.play(Succession(FadeIn(s7_s),FadeOut(s7_s,run_time=0.4),FadeIn(s7_ss)))

        self.wait()
