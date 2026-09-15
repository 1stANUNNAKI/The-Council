import json

# 1. Load the 198 authentic border coordinates
coords = json.load(open('iraq_3d_contour.json'))
coords_js = json.dumps(coords)

html_path = 'majlis_interactive_city.html'
content = open(html_path, encoding='utf-8').read()

missing_block = f'''    /* -------------------------------------------------------------------------
       CUSTOM KINETIC CURSOR & 3D HOVER RAYCASTING
       ------------------------------------------------------------------------- */
    let hoveredIsland = null;
    function onPointerMove(event) {{
      const dot = document.getElementById('cursor-dot');
      const ring = document.getElementById('cursor-ring');
      const badge = document.getElementById('island-hover-badge');

      if (dot && ring) {{
        dot.style.transform = `translate(${{event.clientX}}px, ${{event.clientY}}px) translate(-50%, -50%)`;
        gsap.to(ring, {{
          x: event.clientX,
          y: event.clientY,
          duration: 0.15,
          ease: 'power2.out'
        }});
      }}

      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);

      const targetMeshes = [];
      characterAvatars.forEach(c => {{
        c.traverse(child => {{
          if (child.isMesh) {{
            child.userData.charRoot = c;
            targetMeshes.push(child);
          }}
        }});
      }});
      continentObjects.forEach(cont => {{
        cont.traverse(child => {{
          if (child.isMesh) {{
            child.userData.islandRoot = cont;
            targetMeshes.push(child);
          }}
        }});
      }});

      const intersects = raycaster.intersectObjects(targetMeshes);
      let isHoveringInteractive = false;
      hoveredIsland = null;

      if (intersects.length > 0) {{
        const hitObj = intersects[0].object;
        if (hitObj.userData.charRoot) {{
          isHoveringInteractive = true;
          const char = hitObj.userData.charRoot;
          const ag = DATA.agents.find(a => a.id === char.userData.agentId);
          if (ag && badge) {{
            badge.style.display = 'block';
            badge.style.left = `${{event.clientX}}px`;
            badge.style.top = `${{event.clientY}}px`;
            badge.innerHTML = `${{ag.emoji}} <b>${{state.lang === 'ar' ? ag.name_ar : ag.name_en}}</b> — ${{state.lang === 'ar' ? ag.title_ar : ag.title_en}}`;
          }}
        }} else if (hitObj.userData.islandRoot) {{
          isHoveringInteractive = true;
          const island = hitObj.userData.islandRoot;
          hoveredIsland = island;
          const div = DATA.divisions.find(d => d.id === island.userData.divId);
          if (div && badge) {{
            badge.style.display = 'block';
            badge.style.left = `${{event.clientX}}px`;
            badge.style.top = `${{event.clientY}}px`;
            badge.innerHTML = `${{div.icon}} <b>${{state.lang === 'ar' ? div.name_ar : div.name_en}}</b>`;
          }}
        }}
      }}

      if (!isHoveringInteractive && badge) {{
        badge.style.display = 'none';
      }}
      document.body.classList.toggle('cursor-hover', isHoveringInteractive);
    }}

    function onPointerDown(event) {{
      const rect = renderer.domElement.getBoundingClientRect();
      mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);

      const charMeshes = [];
      characterAvatars.forEach(c => {{
        c.traverse(child => {{
          if (child.isMesh) {{
            child.userData.charRoot = c;
            charMeshes.push(child);
          }}
        }});
      }});

      const islandMeshes = [];
      continentObjects.forEach(cont => {{
        cont.traverse(child => {{
          if (child.isMesh) {{
            child.userData.islandRoot = cont;
            islandMeshes.push(child);
          }}
        }});
      }});

      const charHits = raycaster.intersectObjects(charMeshes);
      if (charHits.length > 0) {{
        const hit = charHits[0].object.userData.charRoot;
        if (hit && hit.userData.agentId) {{
          selectAgent(hit.userData.agentId, true);
          return;
        }}
      }}

      const islandHits = raycaster.intersectObjects(islandMeshes);
      if (islandHits.length > 0) {{
        const hit = islandHits[0].object.userData.islandRoot;
        if (hit && hit.userData.divId) {{
          flyToContinent(hit.userData.divId);
          openContinentInfo(hit.userData.divId);
        }}
      }}
    }}

    function openContinentInfo(divId) {{
      const div = DATA.divisions.find(d => d.id === divId);
      if (!div) return;
      openLayerModal('divisions');
    }}

    function updateSceneAtmosphere() {{
      const isDark = state.theme === 'dark';
      const bgColor = isDark ? 0x070b16 : 0xecf3f9;
      scene.background = new THREE.Color(bgColor);
      scene.fog = new THREE.FogExp2(bgColor, 0.0035);
    }}

    function setupVibrantLighting() {{
      ambientLight = new THREE.AmbientLight(0xffffff, state.theme === 'dark' ? 1.1 : 1.5);
      scene.add(ambientLight);

      dirLight = new THREE.DirectionalLight(0xfff5e6, state.theme === 'dark' ? 1.6 : 1.8);
      dirLight.position.set(120, 220, 140);
      dirLight.castShadow = true;
      dirLight.shadow.mapSize.width = 2048;
      dirLight.shadow.mapSize.height = 2048;
      dirLight.shadow.bias = -0.0004;
      scene.add(dirLight);

      const pLight1 = new THREE.PointLight(0x06b6d4, 1.8, 350);
      pLight1.position.set(-90, 60, -60);
      scene.add(pLight1);

      const pLight2 = new THREE.PointLight(0xf59e0b, 1.8, 350);
      pLight2.position.set(90, 60, 60);
      scene.add(pLight2);
    }}

    /* -------------------------------------------------------------------------
       1. GRAND TERRAIN: AUTHENTIC 3D CRADLE OF IRAQ (خارطة العراق الكبرى الثلاثية الأبعاد)
       ------------------------------------------------------------------------- */
    const IRAQ_GEO_COORDS = {coords_js};

    function createAuthenticIraqTexture() {{
      const canvas = document.createElement('canvas');
      canvas.width = 2048;
      canvas.height = 1650;
      const ctx = canvas.getContext('2d');
      const isDark = state.theme === 'dark';

      // Base background gradient matching architectural model
      const bgGrad = ctx.createRadialGradient(1024, 825, 80, 1024, 825, 1150);
      if (isDark) {{
        bgGrad.addColorStop(0, '#162238');
        bgGrad.addColorStop(0.45, '#0f172a');
        bgGrad.addColorStop(1, '#070b14');
      }} else {{
        bgGrad.addColorStop(0, '#f8fafc');
        bgGrad.addColorStop(0.5, '#e2e8f0');
        bgGrad.addColorStop(1, '#cbd5e1');
      }}
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Engraved horizontal laser relief scanlines matching iraqmapimg.webp
      const lineSpacing = 6;
      const totalLines = Math.floor(canvas.height / lineSpacing);
      for (let l = 0; l < totalLines; l++) {{
        const y = l * lineSpacing;
        const reliefNoise = Math.sin(y * 0.02) * Math.cos(y * 0.045);
        const isMountainZone = y < 520;
        const alpha = isMountainZone ? (0.28 + Math.abs(reliefNoise) * 0.42) : (0.12 + Math.abs(reliefNoise) * 0.22);

        ctx.strokeStyle = isDark ? `rgba(56, 189, 248, ${{alpha}})` : `rgba(15, 23, 42, ${{alpha * 1.3}})`;
        ctx.lineWidth = isMountainZone ? (2.2 + Math.abs(reliefNoise) * 2.0) : (1.2 + Math.abs(reliefNoise) * 1.4);

        ctx.beginPath();
        ctx.moveTo(0, y);
        for (let x = 0; x <= canvas.width; x += 64) {{
          const wave = Math.sin(x * 0.008 + y * 0.015) * 2.2;
          ctx.lineTo(x, y + wave);
        }}
        ctx.stroke();
      }}

      // Topographical contour rings for elevation cues
      ctx.strokeStyle = isDark ? 'rgba(245, 158, 11, 0.12)' : 'rgba(37, 99, 235, 0.12)';
      ctx.lineWidth = 1.5;
      for (let r = 180; r < 900; r += 140) {{
        ctx.beginPath();
        ctx.ellipse(1080, 720, r * 1.25, r * 0.85, -0.15, 0, Math.PI * 2);
        ctx.stroke();
      }}

      const tex = new THREE.CanvasTexture(canvas);
      tex.wrapS = THREE.ClampToEdgeWrapping;
      tex.wrapT = THREE.ClampToEdgeWrapping;
      tex.anisotropy = 16;
      return tex;
    }}

    function buildGrandIraqMap() {{
      const iraqShape = new THREE.Shape();
      iraqShape.moveTo(IRAQ_GEO_COORDS[0][0], IRAQ_GEO_COORDS[0][1]);
      for (let i = 1; i < IRAQ_GEO_COORDS.length; i++) {{
        iraqShape.lineTo(IRAQ_GEO_COORDS[i][0], IRAQ_GEO_COORDS[i][1]);
      }}

      // Massive 3D sovereign base with precision bevel
      const extrudeSettings = {{
        depth: 22,
        bevelEnabled: true,
        bevelSegments: 6,
        steps: 3,
        bevelSize: 6.0,
        bevelThickness: 6.0
      }};

      const iraqGeom = new THREE.ExtrudeGeometry(iraqShape, extrudeSettings);
      iraqGeom.rotateX(Math.PI / 2); // Lay flat on XZ plane

      // Custom Planar UV Mapping across the 320x260 bounding box
      const posAttr = iraqGeom.attributes.position;
      const uvAttr = iraqGeom.attributes.uv;
      const minX = -160, width = 320;
      const minZ = -129, depth = 258;

      for (let i = 0; i < posAttr.count; i++) {{
        const x = posAttr.getX(i);
        const y = posAttr.getY(i);
        const z = posAttr.getZ(i);
        if (y > -2) {{
          const u = (x - minX) / width;
          const v = (z - minZ) / depth;
          uvAttr.setXY(i, u, 1 - v);
        }} else {{
          uvAttr.setXY(i, (x + 160) / 45, (y + 22) / 22);
        }}
      }}
      uvAttr.needsUpdate = true;

      const isDark = state.theme === 'dark';
      const reliefTex = createAuthenticIraqTexture();

      const iraqMat = new THREE.MeshStandardMaterial({{
        color: isDark ? 0x141f33 : 0xe2ebf5,
        map: reliefTex,
        roughness: 0.38,
        metalness: 0.42
      }});

      const iraqBaseMesh = new THREE.Mesh(iraqGeom, iraqMat);
      iraqBaseMesh.position.y = -11;
      iraqBaseMesh.receiveShadow = true;
      scene.add(iraqBaseMesh);

      // Top surface architectural facet wireframe lines
      const wireGeom = new THREE.WireframeGeometry(iraqGeom);
      const wireMat = new THREE.LineBasicMaterial({{
        color: isDark ? 0x243b5e : 0x94a3b8,
        transparent: true,
        opacity: 0.38
      }});
      const wireMesh = new THREE.LineSegments(wireGeom, wireMat);
      wireMesh.position.y = -10.9;
      scene.add(wireMesh);

      // Glowing Sovereign Boundary Parapet Wall (198 border points)
      const borderPoints = IRAQ_GEO_COORDS.map(pt => new THREE.Vector3(pt[0], 0.9, pt[1]));
      const borderCurve = new THREE.CatmullRomCurve3(borderPoints, true);
      const borderWallGeom = new THREE.TubeGeometry(borderCurve, 320, 1.8, 8, true);
      const borderWallMat = new THREE.MeshStandardMaterial({{
        color: isDark ? 0xf59e0b : 0x2563eb,
        roughness: 0.25,
        metalness: 0.85,
        emissive: isDark ? 0xb45309 : 0x1d4ed8,
        emissiveIntensity: 0.45
      }});
      const borderWall = new THREE.Mesh(borderWallGeom, borderWallMat);
      borderWall.position.y = 0.5;
      scene.add(borderWall);

      // Neon Sovereign Crest Line
      const neonBorderGeom = new THREE.BufferGeometry().setFromPoints(borderPoints);
      const neonBorderMat = new THREE.LineBasicMaterial({{
        color: 0x38bdf8,
        linewidth: 3
      }});
      const neonLine = new THREE.Line(neonBorderGeom, neonBorderMat);
      neonLine.position.y = 2.6;
      scene.add(neonLine);

      // Northern Mountain Arc (كردستان وجبال الشمال) - Outside all islands
      const mountainGroup = new THREE.Group();
      for (let i = 0; i < 30; i++) {{
        const h = 22 + Math.random() * 26;
        const mGeom = new THREE.ConeGeometry(8 + Math.random() * 7, h, 5);
        const mMat = new THREE.MeshStandardMaterial({{
          color: isDark ? 0x1e293b : 0x94a3b8,
          roughness: 0.85,
          flatShading: true
        }});
        const mMesh = new THREE.Mesh(mGeom, mMat);
        // Strictly placed in northern mountain ridge (x: 18 to 78, z: -126 to -106)
        mMesh.position.set(
          18 + Math.random() * 60,
          h / 2,
          -126 + Math.random() * 20
        );
        mMesh.castShadow = true;
        mountainGroup.add(mMesh);
      }}
      scene.add(mountainGroup);
    }}

    /* -------------------------------------------------------------------------
       2. THE TWO RIVERS: TIGRIS & EUPHRATES (نهر دجلة والفرات وشط العرب)
       ------------------------------------------------------------------------- */
    function buildTwoRiversOfMesopotamia() {{
      // 1. Tigris River (دجلة) flowing naturally between islands
      const tigrisPts = [
        new THREE.Vector3(-49, 0.8, -120),  // Faysh Khabur entry
        new THREE.Vector3(-30, 0.8, -102),
        new THREE.Vector3(-22, 0.8, -92),   // Mosul / East of Nineveh
        new THREE.Vector3(-8, 0.8, -50),    // Tikrit
        new THREE.Vector3(-2, 0.8, -30),    // Samarra
        new THREE.Vector3(14, 0.8, -3),     // Baghdad (Ground level beneath sky island)
        new THREE.Vector3(40, 0.8, 12),
        new THREE.Vector3(58, 0.8, 24),     // Kut
        new THREE.Vector3(95, 0.8, 45),     // Amarah
        new THREE.Vector3(108, 0.8, 68)     // Qurna (Confluence)
      ];
      const tigrisCurve = new THREE.CatmullRomCurve3(tigrisPts);
      const tigrisGeom = new THREE.TubeGeometry(tigrisCurve, 120, 2.0, 8, false);

      // 2. Euphrates River (الفرات) flowing through western plateau & central basin
      const euphratesPts = [
        new THREE.Vector3(-91, 0.8, -35),   // Al-Qaim border entry
        new THREE.Vector3(-63, 0.8, -38),   // Rawa / Anah
        new THREE.Vector3(-49, 0.8, -28),   // Haditha
        new THREE.Vector3(-35, 0.8, -13),   // Hit
        new THREE.Vector3(-20, 0.8, -6),    // Ramadi
        new THREE.Vector3(-5, 0.8, -4),     // Fallujah
        new THREE.Vector3(12, 0.8, 18),
        new THREE.Vector3(18, 0.8, 30),     // Babylon / Hillah
        new THREE.Vector3(42, 0.8, 55),     // Samawa
        new THREE.Vector3(72, 0.8, 66),     // Nasiriyah
        new THREE.Vector3(108, 0.8, 68)     // Qurna (Confluence)
      ];
      const euphratesCurve = new THREE.CatmullRomCurve3(euphratesPts);
      const euphratesGeom = new THREE.TubeGeometry(euphratesCurve, 120, 2.0, 8, false);

      // 3. Shatt al-Arab (شط العرب) to Al-Faw & Arabian Gulf
      const shattPts = [
        new THREE.Vector3(108, 0.8, 68),    // Qurna
        new THREE.Vector3(121, 0.8, 84),    // Basra
        new THREE.Vector3(128, 0.8, 88),    // Abu al-Khasib
        new THREE.Vector3(142, 0.8, 102)    // Al-Faw / Gulf
      ];
      const shattCurve = new THREE.CatmullRomCurve3(shattPts);
      const shattGeom = new THREE.TubeGeometry(shattCurve, 50, 3.2, 8, false);

      const riverMat = new THREE.MeshBasicMaterial({{
        color: 0x06b6d4,
        transparent: true,
        opacity: 0.92
      }});

      const tigrisMesh = new THREE.Mesh(tigrisGeom, riverMat);
      const euphratesMesh = new THREE.Mesh(euphratesGeom, riverMat);
      const shattMesh = new THREE.Mesh(shattGeom, riverMat);

      scene.add(tigrisMesh);
      scene.add(euphratesMesh);
      scene.add(shattMesh);

      riverLines.push(tigrisMesh, euphratesMesh, shattMesh);
    }}
'''

# Find insertion point right after `animate();\n    }` in init3D
target_marker = "      // Animation Loop\n      animate();\n    }\n"
assert target_marker in content, "target marker not found!"

content = content.replace(target_marker, target_marker + "\n" + missing_block)
open(html_path, 'w', encoding='utf-8').write(content)
print("Successfully assembled complete 3D scene functions!")
