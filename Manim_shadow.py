from manim import*

class shadows(Scene): 
    def construct(self):
        
        square = Square(side_length=7).set_fill(GREY,opacity=1)
        line1 = Line(start=[-3,0,0], end=[3,0,0], stroke_width=30)
        line2 = Line(start=[0,3,0], end=[0,-3,0], stroke_width=30)
        circle = Arc(radius=1, angle=PI * 2, start_angle=1.5708, stroke_width=30)

        #Adding shadows
        line1_s = Line(start=[-3,0,0],end=[3,0,0], stroke_width=30, stroke_color=BLACK)
        line2_s = Line(start=[0,3,0], end=[0,-3,0], stroke_width=30,stroke_color=BLACK)
        circle_s = Arc(radius=1, angle=PI * 2, start_angle=1.5708, stroke_width=30, stroke_color=BLACK)
        
        #Shifting shadows
        line1_s.shift(DOWN*0.2+RIGHT*0.2)
        line2_s.shift(DOWN*0.1+RIGHT*0.2)
        circle_s.shift(DOWN*0.2+RIGHT*0.2)

        #Adding depth using z-index
        line1.set_z_index(6)
        line1_s.set_z_index(5)
        line2.set_z_index(4)
        line2_s.set_z_index(3)
        circle.set_z_index(2)
        circle_s.set_z_index(1)

        #Enhancing shadows
        line1_s.set_opacity(0.5)
        line2_s.set_opacity(0.5)
        circle_s.set_opacity(0.5)

        self.play(Create(square))
        self.play(Create(circle))
        self.wait()
        self.play(Create(line1))
        self.wait()
        self.play(Create(line2))
        self.wait()
        
        #Animate Shadows
        self.play(Create(line1_s))
        self.wait()
        self.play(Create(line2_s))
        self.wait()
        self.play(Create(circle_s))
        self.wait()
