from manim import *
from manim_slides import ThreeDSlide
import random
import numpy as np

config.background_color = "#020617"

class Welcome(ThreeDSlide):
    def construct(self):
        UI_MUTED = "#94A3B8"
        ACCENT   = "#38BDF8"

        # Real 3D camera motion (cheap)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-35 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.12)

        # ---- Graph setup (keep modest = fast) ----
        n = 35
        m_edges = 85
        vertices = list(range(n))

        edges = set()
        while len(edges) < m_edges:
            a, b = random.sample(vertices, 2)
            edges.add((min(a, b), max(a, b)))
        edges = list(edges)

        # ✅ REAL 3D positions (nonzero Z!)
        layout = {
            v: np.array([
                random.uniform(-3.0, 3.0),
                random.uniform(-2.0, 2.0),
                random.uniform(-2.5, 2.5),
            ])
            for v in vertices
        }

        # ✅ True 3D dots (spheres), but LOW resolution so it's not heavy
        g = Graph(
            vertices,
            edges,
            layout=layout,
            vertex_type=Dot3D,          # Graph allows any Mobject as vertex_type :contentReference[oaicite:2]{index=2}
            edge_type=Line,             # keep edges thin + cheap
            vertex_config={
                "radius": 0.05,
                "resolution": (4, 4),   # big speed win; Dot3D supports resolution :contentReference[oaicite:3]{index=3}
                "color": UI_MUTED,
            },
            edge_config={
                "stroke_opacity": 0.10,
                "stroke_width": 1,
                "color": UI_MUTED,
            },
        )

        # 1) Appear
        self.play(Create(g), run_time=1.2)
        self.next_slide(loop=True)

        # 2) Let it orbit (this is where it looks 3D)
        self.play(Wait(3.5))
        self.next_slide(loop=True)
        
        # 3) Move some vertices (edges follow automatically)
        movers = random.sample(vertices, 8)
        self.play(*[
            g[v].animate.move_to([
                random.uniform(-3.0, 3.0),
                random.uniform(-2.0, 2.0),
                random.uniform(-2.5, 2.5),
            ])
            for v in movers
        ], run_time=1.6)

        # 4) “Neural firing” pulse
        some_edges = random.sample(list(g.edges.values()), k=22)
        pulse = VGroup(*some_edges)
        self.play(pulse.animate.set_stroke(color=ACCENT, opacity=0.85, width=2), run_time=0.25)
        self.play(pulse.animate.set_stroke(color=UI_MUTED, opacity=0.10, width=1), run_time=0.55)

        # 5) End hold
        self.play(Wait(2.0))

        self.stop_ambient_camera_rotation()