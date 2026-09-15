import re

html_path = 'majlis_interactive_city.html'
content = open(html_path, encoding='utf-8').read()

# Replace createAuthenticIraqTexture with higher-contrast, glowing laser relief lines matching iraqmapimg.webp
replacement_texture_func = '''    function createAuthenticIraqTexture() {
      const canvas = document.createElement('canvas');
      canvas.width = 2048;
      canvas.height = 1650;
      const ctx = canvas.getContext('2d');
      const isDark = state.theme === 'dark';

      // 1. Sleek metallic architectural background
      const bgGrad = ctx.createLinearGradient(0, 0, 0, canvas.height);
      if (isDark) {
        bgGrad.addColorStop(0, '#1a273e');
        bgGrad.addColorStop(0.35, '#121d2f');
        bgGrad.addColorStop(0.7, '#0d1522');
        bgGrad.addColorStop(1, '#070b13');
      } else {
        bgGrad.addColorStop(0, '#ffffff');
        bgGrad.addColorStop(0.4, '#f1f5f9');
        bgGrad.addColorStop(0.8, '#e2e8f0');
        bgGrad.addColorStop(1, '#cbd5e1');
      }
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // 2. High-contrast horizontal laser scanline relief grooves matching iraqmapimg.webp
      const lineSpacing = 5;
      const totalLines = Math.floor(canvas.height / lineSpacing);
      for (let l = 0; l < totalLines; l++) {
        const y = l * lineSpacing;
        const reliefNoise = Math.sin(y * 0.022) * Math.cos(y * 0.048);
        const isMountainZone = y < 520;
        
        // Dynamic contrasting alpha
        const alpha = isMountainZone 
          ? (0.55 + Math.abs(reliefNoise) * 0.42) 
          : (0.35 + Math.abs(reliefNoise) * 0.35);

        if (isDark) {
          ctx.strokeStyle = isMountainZone ? `rgba(56, 189, 248, ${alpha})` : `rgba(148, 163, 184, ${alpha * 0.75})`;
        } else {
          ctx.strokeStyle = isMountainZone ? `rgba(15, 23, 42, ${alpha * 1.1})` : `rgba(51, 65, 85, ${alpha * 0.85})`;
        }
        ctx.lineWidth = isMountainZone ? (2.4 + Math.abs(reliefNoise) * 2.2) : (1.4 + Math.abs(reliefNoise) * 1.6);

        ctx.beginPath();
        ctx.moveTo(0, y);
        for (let x = 0; x <= canvas.width; x += 48) {
          const wave = Math.sin(x * 0.01 + y * 0.018) * 2.8;
          ctx.lineTo(x, y + wave);
        }
        ctx.stroke();
      }

      // 3. Topographical relief contour rings
      for (let r = 120; r < 950; r += 110) {
        ctx.strokeStyle = isDark ? 'rgba(245, 158, 11, 0.22)' : 'rgba(37, 99, 235, 0.25)';
        ctx.lineWidth = 2.0;
        ctx.beginPath();
        ctx.ellipse(1080, 720, r * 1.25, r * 0.85, -0.12, 0, Math.PI * 2);
        ctx.stroke();
      }

      // 4. Subtle holographic coordinate grid
      ctx.strokeStyle = isDark ? 'rgba(56, 189, 248, 0.08)' : 'rgba(0, 0, 0, 0.08)';
      ctx.lineWidth = 1;
      for (let x = 0; x < canvas.width; x += 128) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();
      }

      const tex = new THREE.CanvasTexture(canvas);
      tex.wrapS = THREE.ClampToEdgeWrapping;
      tex.wrapT = THREE.ClampToEdgeWrapping;
      tex.anisotropy = 16;
      return tex;
    }'''

# Replace createAuthenticIraqTexture
pattern_tex = re.compile(r'function createAuthenticIraqTexture\(\) \{[\s\S]+?return tex;\s*\}', re.MULTILINE)
assert pattern_tex.search(content), "createAuthenticIraqTexture not found!"
content = pattern_tex.sub(replacement_texture_func, content)

# Enhance material settings in buildGrandIraqMap
content = content.replace(
    "color: isDark ? 0x141f33 : 0xe2ebf5,\n        map: reliefTex,\n        roughness: 0.38,\n        metalness: 0.42",
    "color: isDark ? 0x22324e : 0xffffff,\n        map: reliefTex,\n        emissive: isDark ? 0x091424 : 0x000000,\n        roughness: 0.32,\n        metalness: 0.45"
)

# Update initial camera and controls target for perfect overview
content = content.replace(
    "camera.position.set(0, 160, 210);",
    "camera.position.set(0, 240, 260);"
)
content = content.replace(
    "controls.target.set(0, 8, 0);",
    "controls.target.set(0, 4, 10);"
)
content = content.replace(
    "if (cam === 'overview') flyCameraTo({ x: 0, y: 210, z: 270 }, { x: 0, y: 8, z: 0 });",
    "if (cam === 'overview') flyCameraTo({ x: 0, y: 240, z: 260 }, { x: 0, y: 4, z: 10 });"
)
content = content.replace(
    "flyCameraTo({ x: 0, y: 210, z: 270 }, { x: 0, y: 8, z: 0 });",
    "flyCameraTo({ x: 0, y: 240, z: 260 }, { x: 0, y: 4, z: 10 });"
)

open(html_path, 'w', encoding='utf-8').write(content)
print("Successfully enhanced Iraq map texture contrast and camera overview positioning!")
