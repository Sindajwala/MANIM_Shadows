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


         text3 = Text('Adding Depth Using Z-Index').shift(UP*1)
        s8 = Ellipse().next_to(text3,DOWN).set_z_index(7)
        s9 = Ellipse().next_to(text3,DOWN*2).scale(0.7).set_z_index(6)
        s10 = Ellipse().next_to(text3,DOWN*3).scale(0.3).set_z_index(5)
        s11 = Ellipse().next_to(text3,DOWN*5).scale(0.3).set_z_index(3)
        s12 = Ellipse().next_to(text3,DOWN*6).scale(0.7).set_z_index(2)
        s13 = Ellipse().next_to(text3,DOWN*7).set_z_index(1)
        plane = NumberPlane(
            x_length=2,
            y_length=1,
        )
        matrix = [[1, 1], [0, 1]]
        plane.apply_matrix(matrix).next_to(text3,DOWN*4).set_z_index(4)
        dshl1 = DashedLine(start=ORIGIN,end=UP*2)
        darrow1 = Arrow(start=UP*2,end=UP*2)
        arrow_group1 = VGroup(dshl1, darrow1)
        dshl2 = DashedLine(start=ORIGIN,end=DOWN*2)
        darrow2 = Arrow(start=DOWN*2,end=DOWN*2)
        arrow_group2 = VGroup(dshl2, darrow2)

        self.play(Succession(Create(text3),Circumscribe(text3)))
        self.wait()
        self.play(FadeIn(plane))
        self.wait()
        self.play(Succession(Create(VGroup(s10,s11)),Create(VGroup(s9,s12)),Create(VGroup(s8,s13))))
        self.wait()
        self.play(Create(arrow_group1),Create(arrow_group2))
        self.wait(2)
