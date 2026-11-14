from __future__ import annotations
import html as html_lib
from docutils import nodes
from docutils.parsers.rst import Directive, directives

def _parse_ratio(ratio_str: str) -> tuple[int, int]:
    parts = ratio_str.strip().split(":")
    if len(parts) != 2:
        return 16, 9 # Default fallback
    return int(parts[0]), int(parts[1])

class VideoDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False

    option_spec = {
        "caption": directives.unchanged,
        "ratio": directives.unchanged,
        "max-width": directives.unchanged,
        "start": directives.nonnegative_int,
        "align": directives.unchanged,
        "height": directives.unchanged, # Ignored, but accepted
    }

    def run(self):
        vid = self.arguments[0].strip()
        caption = self.options.get("caption", "").strip()
        ratio = self.options.get("ratio", "16:9").strip()
        max_width = self.options.get("max-width", "").strip()
        start = self.options.get("start", None)
        align = self.options.get("align", "center").strip()

        w, h = _parse_ratio(ratio)

        # 1. Build Styles for the OUTER Wrapper (Width & Alignment)
        wrapper_styles = []
        if max_width:
            wrapper_styles.append(f"max-width:{max_width};")
        
        # Handle Alignment
        if align == "left":
            wrapper_styles.append("margin-right: auto; margin-left: 0;")
        elif align == "right":
            wrapper_styles.append("margin-left: auto; margin-right: 0;")
        else:
            wrapper_styles.append("margin-left: auto; margin-right: auto;")
            
        wrapper_attr = " ".join(wrapper_styles)

        # 2. Build Styles for the INNER Video Container (Aspect Ratio)
        container_style = f"aspect-ratio:{w}/{h}; position:relative; width:100%;"

        # 3. Build URL
        src = f"https://www.youtube.com/embed/{vid}"
        if start is not None and start > 0:
            src += f"?start={start}"

        # 4. Construct HTML
        html = []
        # Open Outer Wrapper
        html.append(f'<div class="video-wrapper" style="{wrapper_attr}">')
        
        # Video Container
        html.append(f'  <div class="video-container" style="{container_style}">')
        html.append(f'    <iframe src="{src}" allowfullscreen style="width:100%; height:100%; position:absolute; left:0; top:0; border:0;" loading="lazy"></iframe>')
        html.append(f'  </div>')

        # Caption (Inside Wrapper)
        if caption:
            safe_caption = html_lib.escape(caption)
            html.append(f'  <div class="video-caption" style="margin-top:0.5em; text-align:left; color:#666;">{safe_caption}</div>')
        
        # Close Outer Wrapper
        html.append('</div>')

        return [nodes.raw("", "\n".join(html), format="html")]
# ... (Keep your imports and _parse_ratio function at the top) ...

# ... (Keep your existing VideoDirective class here) ...

class PhetDirective(Directive):
    """
    Usage (MyST):
    
    ```{phet} [https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_en.html](https://phet.colorado.edu/sims/html/projectile-motion/latest/projectile-motion_en.html)
    :caption: Projectile Motion Simulation
    :ratio: 16:9
    :max-width: 800px
    ```
    """
    required_arguments = 1  # The full PhET URL
    optional_arguments = 0
    final_argument_whitespace = False
    has_content = False

    option_spec = {
        "caption": directives.unchanged,
        "ratio": directives.unchanged,
        "max-width": directives.unchanged,
        "align": directives.unchanged,
        "height": directives.unchanged, 
    }

    def run(self):
        # Users should paste the full URL found in the PhET "Embed" code
        src = self.arguments[0].strip()
        
        caption = self.options.get("caption", "").strip()
        ratio = self.options.get("ratio", "16:9").strip() # PhET sims are often 16:9 or 4:3
        max_width = self.options.get("max-width", "").strip()
        align = self.options.get("align", "center").strip()

        w, h = _parse_ratio(ratio)

        # 1. Outer Wrapper (Width & Alignment)
        wrapper_styles = []
        if max_width:
            wrapper_styles.append(f"max-width:{max_width};")
        
        if align == "left":
            wrapper_styles.append("margin-right: auto; margin-left: 0;")
        elif align == "right":
            wrapper_styles.append("margin-left: auto; margin-right: 0;")
        else:
            wrapper_styles.append("margin-left: auto; margin-right: auto;")
            
        wrapper_attr = " ".join(wrapper_styles)

        # 2. Inner Container (Aspect Ratio)
        container_style = f"aspect-ratio:{w}/{h}; position:relative; width:100%;"

        # 3. Construct HTML
        html = []
        html.append(f'<div class="phet-wrapper" style="{wrapper_attr}">')
        html.append(f'  <div class="phet-container" style="{container_style}">')
        html.append(f'    <iframe src="{src}" allowfullscreen style="width:100%; height:100%; position:absolute; left:0; top:0; border:0;" scrolling="no"></iframe>')
        html.append(f'  </div>')

        if caption:
            safe_caption = html_lib.escape(caption)
            html.append(f'  <div class="phet-caption" style="margin-top:0.5em; text-align:center; color:#666;">{safe_caption}</div>')
        
        html.append('</div>')

        return [nodes.raw("", "\n".join(html), format="html")]

def setup(app):
    app.add_directive("etamu-video", VideoDirective)
    # Register the new directive here
    app.add_directive("phet", PhetDirective) 

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
