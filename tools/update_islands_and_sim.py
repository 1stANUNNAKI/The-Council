import re

html_path = 'majlis_interactive_city.html'
content = open(html_path, encoding='utf-8').read()

# 1. Replacement for createSculptedIslandMesh & buildDiverseContinents
replacement_continents_code = '''    /* -------------------------------------------------------------------------
       3. SCULPTED 3D FLOATING ISLANDS (مجسمات جزر طافية حقيقية غنية وغير متداخلة)
       ------------------------------------------------------------------------- */
    function createSculptedIslandMesh(w, h, d, colorHex, isSkyIsland = false) {
      const islandGroup = new THREE.Group();
      const isDark = state.theme === 'dark';

      // 1. Lush Architectural Plateau Top (السطح المعماري الرئيسي للجزيرة)
      const topGeom = new THREE.CylinderGeometry(w / 2, (w / 2) * 1.08, h * 0.45, 24);
      const topMat = new THREE.MeshStandardMaterial({
        color: isSkyIsland ? 0x1e293b : (isDark ? 0x152238 : 0xdce7f3),
        roughness: 0.35,
        metalness: 0.38
      });
      const topMesh = new THREE.Mesh(topGeom, topMat);
      topMesh.position.y = h * 0.22;
      topMesh.receiveShadow = true;
      islandGroup.add(topMesh);

      // Inner decorative terraced sub-plateau (طبقة معمارية داخلية متدرجة تزيد فخامة الجزيرة)
      const subGeom = new THREE.CylinderGeometry(w * 0.4, w * 0.44, h * 0.22, 20);
      const subMat = new THREE.MeshStandardMaterial({
        color: isDark ? 0x0f172a : 0xf1f5f9,
        roughness: 0.45,
        metalness: 0.25
      });
      const subMesh = new THREE.Mesh(subGeom, subMat);
      subMesh.position.y = h * 0.52;
      subMesh.receiveShadow = true;
      islandGroup.add(subMesh);

      // 2. Natural Rugged Inverted Rocky Underbelly (قاع صخري مجسم متدرج للأسفل بطبقتين)
      const underGeom = new THREE.ConeGeometry((w / 2) * 1.06, h * 1.35, 14);
      underGeom.rotateX(Math.PI);
      const underMat = new THREE.MeshStandardMaterial({
        color: isDark ? 0x0a101d : 0x64748b,
        roughness: 0.9,
        metalness: 0.15,
        flatShading: true
      });
      const underMesh = new THREE.Mesh(underGeom, underMat);
      underMesh.position.y = -h * 0.68;
      underMesh.castShadow = true;
      islandGroup.add(underMesh);

      // Secondary jagged rock stalactites hanging from the underbelly
      for (let r = 0; r < 6; r++) {
        const angle = (r / 6) * Math.PI * 2;
        const rad = (w / 2) * 0.68;
        const stGeom = new THREE.ConeGeometry(w * 0.08, h * 0.8, 6);
        stGeom.rotateX(Math.PI);
        const stMesh = new THREE.Mesh(stGeom, underMat);
        stMesh.position.set(Math.cos(angle) * rad, -h * 0.4, Math.sin(angle) * rad);
        islandGroup.add(stMesh);
      }

      // 3. Glowing Energy Geode / Levitation Crystal Cluster at bottom tip
      const crystalGeom = new THREE.OctahedronGeometry(w * 0.18, 0);
      const crystalMat = new THREE.MeshBasicMaterial({ color: colorHex });
      const crystal = new THREE.Mesh(crystalGeom, crystalMat);
      crystal.position.y = -h * 1.35;
      islandGroup.add(crystal);

      // Orbiting energy ring around crystal
      const cRingGeom = new THREE.TorusGeometry(w * 0.25, 0.45, 6, 20);
      cRingGeom.rotateX(Math.PI / 2.3);
      const cRing = new THREE.Mesh(cRingGeom, new THREE.MeshBasicMaterial({ color: colorHex, wireframe: true }));
      cRing.position.y = -h * 1.35;
      islandGroup.add(cRing);

      // 4. Luminous Double Island Boundary Rings
      const rimGeom = new THREE.TorusGeometry((w / 2) * 1.05, 0.6, 6, 36);
      rimGeom.rotateX(Math.PI / 2);
      const rim = new THREE.Mesh(rimGeom, new THREE.MeshBasicMaterial({ color: colorHex }));
      rim.position.y = h * 0.45;
      islandGroup.add(rim);

      const rimGeom2 = new THREE.TorusGeometry(w * 0.4, 0.4, 6, 28);
      rimGeom2.rotateX(Math.PI / 2);
      const rim2 = new THREE.Mesh(rimGeom2, new THREE.MeshBasicMaterial({ color: colorHex, transparent: true, opacity: 0.65 }));
      rim2.position.y = h * 0.62;
      islandGroup.add(rim2);

      return islandGroup;
    }

    function buildDiverseContinents() {
      // Expanded scale factor (1.8x) to make all islands expansive and magnificent
      const scaleMultiplier = 1.8;

      DATA.divisions.forEach(div => {
        const group = new THREE.Group();
        const isSkyIsland = div.id === 'lead';
        const posY = isSkyIsland ? 38 : div.coords.y;
        group.position.set(div.coords.x, posY, div.coords.z);

        const color = new THREE.Color(div.color);
        const isDark = state.theme === 'dark';

        const scaledW = div.scale.x * scaleMultiplier;
        const scaledH = div.scale.y * 1.3;
        const scaledD = div.scale.z * scaleMultiplier;

        // 1. Build Natural Sculpted 3D Floating Island Body
        const islandBody = createSculptedIslandMesh(scaledW, scaledH, scaledD, color, isSkyIsland);
        group.add(islandBody);

        // 2. Rich Distinct Architectural Centerpieces on Top Plateau
        if (div.shape === 'citadel') {
          // Baghdad Golden Sky Citadel (سماء بغداد - الجزيرة العائمة الكبرى)
          const zigguratMat = new THREE.MeshStandardMaterial({
            color: color.clone().multiplyScalar(isDark ? 0.95 : 1.15),
            roughness: 0.2,
            metalness: 0.88
          });
          // 5-tier grand ziggurat
          for (let s = 0; s < 5; s++) {
            const w = 28 - (s * 5);
            const box = new THREE.Mesh(new THREE.CylinderGeometry(w / 2, w / 2 + 1.2, 3.8, 8), zigguratMat);
            box.position.y = scaledH * 0.45 + (s * 3.8) + 1.9;
            box.castShadow = true;
            group.add(box);
          }
          const spire = new THREE.Mesh(new THREE.ConeGeometry(4.0, 22, 8), zigguratMat);
          spire.position.y = scaledH * 0.45 + 28;
          group.add(spire);

          // Rotating celestial octahedron prism atop spire
          const apexPrism = new THREE.Mesh(new THREE.OctahedronGeometry(2.5, 0), new THREE.MeshBasicMaterial({ color: 0xfef08a }));
          apexPrism.position.y = scaledH * 0.45 + 40;
          group.add(apexPrism);

          // 6 Perimeter Celestial Pylons
          for (let c = 0; c < 6; c++) {
            const ang = (c / 6) * Math.PI * 2;
            const rPylon = scaledW * 0.35;
            const pylon = new THREE.Mesh(new THREE.CylinderGeometry(1.0, 1.5, 14, 6), zigguratMat);
            pylon.position.set(Math.cos(ang) * rPylon, scaledH * 0.45 + 7, Math.sin(ang) * rPylon);
            pylon.castShadow = true;
            group.add(pylon);

            // Floating crystal atop each pylon
            const pCrystal = new THREE.Mesh(new THREE.OctahedronGeometry(1.4, 0), new THREE.MeshBasicMaterial({ color: 0xf59e0b }));
            pCrystal.position.set(Math.cos(ang) * rPylon, scaledH * 0.45 + 16, Math.sin(ang) * rPylon);
            group.add(pCrystal);
          }

          // Vertical Golden Energy Cascade connecting Sky Island to Baghdad Ground
          const beamGeom = new THREE.CylinderGeometry(2.2, 2.2, 42, 16, 1, true);
          const beamMat = new THREE.MeshBasicMaterial({
            color: 0xf59e0b,
            transparent: true,
            opacity: 0.72,
            side: THREE.DoubleSide
          });
          const beam = new THREE.Mesh(beamGeom, beamMat);
          beam.position.y = -21;
          group.add(beam);

        } else if (div.shape === 'forge') {
          // Babylon Foundry & Engineering (مسبك ومفاعلات بابل العملاقة)
          const forgeMat = new THREE.MeshStandardMaterial({
            color: 0x10b981,
            roughness: 0.25,
            metalness: 0.8
          });
          // 8 Industrial Cyber Smokestacks & Foundry Reactors
          for (let t = 0; t < 8; t++) {
            const towerH = 14 + (t % 4) * 3.5;
            const tower = new THREE.Mesh(new THREE.CylinderGeometry(2.6, 4.0, towerH, 8), forgeMat);
            const ang = (t / 8) * Math.PI * 2;
            const r = scaledW * 0.28;
            tower.position.set(Math.cos(ang) * r, scaledH * 0.45 + (towerH / 2), Math.sin(ang) * r);
            tower.castShadow = true;
            group.add(tower);

            // Glowing reactor cap
            const cap = new THREE.Mesh(new THREE.CylinderGeometry(2.8, 2.8, 1.2, 8), new THREE.MeshBasicMaterial({ color: 0x34d399 }));
            cap.position.set(Math.cos(ang) * r, scaledH * 0.45 + towerH + 0.6, Math.sin(ang) * r);
            group.add(cap);
          }
          // Central Turbine Dome
          const dome = new THREE.Mesh(
            new THREE.SphereGeometry(9, 20, 14, 0, Math.PI * 2, 0, Math.PI / 2),
            new THREE.MeshStandardMaterial({ color: 0x059669, metalness: 0.9, roughness: 0.2 })
          );
          dome.position.set(0, scaledH * 0.45 + 1, 0);
          group.add(dome);

        } else if (div.shape === 'fortress') {
          // Western Frontier Security Bastion (حصن الأنبار الأمني المصفح)
          const fortMat = new THREE.MeshStandardMaterial({
            color: 0xef4444,
            roughness: 0.35,
            metalness: 0.65
          });
          const bastion = new THREE.Mesh(new THREE.CylinderGeometry(18, 22, 14, 6), fortMat);
          bastion.position.y = scaledH * 0.45 + 7;
          bastion.castShadow = true;
          group.add(bastion);

          // 6 Sentry Laser Turrets around Bastion
          for (let st = 0; st < 6; st++) {
            const sAng = (st / 6) * Math.PI * 2;
            const sRad = scaledW * 0.34;
            const sentry = new THREE.Mesh(new THREE.CylinderGeometry(2.4, 3.4, 11, 6), fortMat);
            sentry.position.set(Math.cos(sAng) * sRad, scaledH * 0.45 + 5.5, Math.sin(sAng) * sRad);
            group.add(sentry);
            const redLaser = new THREE.Mesh(new THREE.ConeGeometry(1.0, 5, 4), new THREE.MeshBasicMaterial({ color: 0xff0000 }));
            redLaser.position.set(Math.cos(sAng) * sRad, scaledH * 0.45 + 13.5, Math.sin(sAng) * sRad);
            group.add(redLaser);
          }

          // Holographic Hexagonal Forcefield Shield Dome
          const shieldDome = new THREE.Mesh(
            new THREE.SphereGeometry(scaledW * 0.42, 16, 12, 0, Math.PI * 2, 0, Math.PI / 2),
            new THREE.MeshBasicMaterial({ color: 0xef4444, wireframe: true, transparent: true, opacity: 0.55 })
          );
          shieldDome.position.y = scaledH * 0.45 + 2;
          group.add(shieldDome);

        } else if (div.shape === 'palace') {
          // Basra Kinetic Arts & Floating Water Terraces (قصور وأهوار البصرة الحركية)
          const palaceMat = new THREE.MeshStandardMaterial({
            color: 0xa855f7,
            roughness: 0.2,
            metalness: 0.68
          });
          // 6 Stepped Lotus Water Pavilions
          for (let p = 0; p < 6; p++) {
            const lotus = new THREE.Mesh(new THREE.CylinderGeometry(9 - p * 1.3, 10 - p * 1.3, 3.5, 16), palaceMat);
            lotus.position.set((p - 2.5) * 10, scaledH * 0.45 + (p * 2.8) + 1.75, ((p % 2) - 0.5) * 8);
            lotus.castShadow = true;
            group.add(lotus);
          }
          // Translucent Lotus Fountain & Kinetic Rings
          const fountainGeom = new THREE.CylinderGeometry(4.5, 4.5, 10, 20);
          const fountainMat = new THREE.MeshStandardMaterial({ color: 0xc084fc, transparent: true, opacity: 0.8, roughness: 0.1 });
          const fountain = new THREE.Mesh(fountainGeom, fountainMat);
          fountain.position.set(0, scaledH * 0.45 + 6, 0);
          group.add(fountain);

          // Crystalline Lotus Bloom atop Fountain
          const bloom = new THREE.Mesh(new THREE.OctahedronGeometry(3.0, 0), new THREE.MeshBasicMaterial({ color: 0xf472b6 }));
          bloom.position.set(0, scaledH * 0.45 + 13, 0);
          group.add(bloom);

        } else if (div.shape === 'observatory') {
          // Northern Mountain Observatory (مراصد وقباب جبال كردستان الفضائية)
          const obsMat = new THREE.MeshStandardMaterial({ color: 0x06b6d4, metalness: 0.78, roughness: 0.25 });
          const needle = new THREE.Mesh(new THREE.ConeGeometry(5.5, 30, 8), obsMat);
          needle.position.y = scaledH * 0.45 + 15;
          needle.castShadow = true;
          group.add(needle);

          // 3 Giant Rotating Radio Telescope Dishes
          for (let d = 0; d < 3; d++) {
            const dAng = (d / 3) * Math.PI * 2;
            const dRad = scaledW * 0.28;
            const dish = new THREE.Mesh(
              new THREE.SphereGeometry(7.5, 20, 10, 0, Math.PI * 2, 0, Math.PI / 2),
              new THREE.MeshStandardMaterial({ color: 0x38bdf8, metalness: 0.9, side: THREE.DoubleSide })
            );
            dish.position.set(Math.cos(dAng) * dRad, scaledH * 0.45 + 14, Math.sin(dAng) * dRad);
            dish.rotateX(Math.PI * 0.65);
            dish.rotateZ(dAng);
            group.add(dish);
          }

        } else {
          // Nineveh Archives & Wisdom Library (مكتبة نينوى الإمبراطورية العظمى)
          const libMat = new THREE.MeshStandardMaterial({ color: 0x3b82f6, metalness: 0.68, roughness: 0.3 });
          // 12-Column Colonnade Pantheon
          for (let c = 0; c < 12; c++) {
            const col = new THREE.Mesh(new THREE.CylinderGeometry(1.4, 1.4, 14, 14), libMat);
            col.position.set(-25 + c * 4.5, scaledH * 0.45 + 7, -10);
            col.castShadow = true;
            group.add(col);
          }
          const arch = new THREE.Mesh(new THREE.BoxGeometry(54, 3.5, 14), libMat);
          arch.position.set(0, scaledH * 0.45 + 15.75, -10);
          group.add(arch);

          // 2 Soaring Obelisks of Knowledge flanking the front plaza
          [-16, 16].forEach(ox => {
            const obelisk = new THREE.Mesh(new THREE.BoxGeometry(3.0, 20, 3.0), new THREE.MeshStandardMaterial({ color: 0x60a5fa, metalness: 0.85 }));
            obelisk.position.set(ox, scaledH * 0.45 + 10, 12);
            group.add(obelisk);
          });

          // 4 Floating Holographic Codex Scrolls
          for (let sc = 0; sc < 4; sc++) {
            const sAng = (sc / 4) * Math.PI * 2;
            const scroll = new THREE.Mesh(
              new THREE.PlaneGeometry(3, 4.5),
              new THREE.MeshBasicMaterial({ color: 0x93c5fd, side: THREE.DoubleSide, transparent: true, opacity: 0.75 })
            );
            scroll.position.set(Math.cos(sAng) * 16, scaledH * 0.45 + 18, Math.sin(sAng) * 16);
            group.add(scroll);
          }
        }

        group.userData = { divId: div.id, isIsland: true, divData: div, scaledW, scaledH, scaledD };
        group.traverse(child => {
          if (child.isMesh) {
            child.userData.islandRoot = group;
          }
        });

        scene.add(group);
        continentObjects.push(group);
      });
    }'''

# Replace buildDiverseContinents and createSculptedIslandMesh
pattern_continents = re.compile(r'/\* -+[\s\S]+?function createSculptedIslandMesh[\s\S]+?scene\.add\(group\);\s*continentObjects\.push\(group\);\s*\}\);?\s*\}', re.MULTILINE)
assert pattern_continents.search(content), "Could not find createSculptedIslandMesh and buildDiverseContinents pattern!"
content = pattern_continents.sub(replacement_continents_code, content)

# 2. Replacement for buildArticulatedAgentCharacters
replacement_agents_code = '''    function buildArticulatedAgentCharacters() {
      const divAgents = {};
      DATA.agents.forEach(agent => {
        const d = agent.division || 'lead';
        if (!divAgents[d]) divAgents[d] = [];
        divAgents[d].push(agent);
      });

      const scaleMultiplier = 1.8;

      DATA.divisions.forEach(div => {
        const list = divAgents[div.id] || [];
        const isSkyIsland = div.id === 'lead';
        const scaledH = div.scale.y * 1.3;
        const scaledW = div.scale.x * scaleMultiplier;
        const scaledD = div.scale.z * scaleMultiplier;

        const islandTopY = (isSkyIsland ? 38 : div.coords.y) + (scaledH * 0.45);
        const radius = Math.min(scaledW, scaledD) * 0.44;

        list.forEach((agent, idx) => {
          const charGroup = new THREE.Group();

          // Non-colliding circular plaza positions around the perimeter
          const angle = (idx / list.length) * Math.PI * 2;
          const posX = div.coords.x + Math.cos(angle) * radius;
          const posZ = div.coords.z + Math.sin(angle) * radius;
          const posY = islandTopY + 0.1;

          charGroup.position.set(posX, posY, posZ);
          charGroup.lookAt(div.coords.x, posY, div.coords.z);

          const color = new THREE.Color(div.color);

          // 1. Anti-Gravity Propulsion Disk (Podium)
          const diskGeom = new THREE.CylinderGeometry(2.8, 3.6, 1.2, 16);
          const diskMat = new THREE.MeshStandardMaterial({
            color: 0x1e293b,
            metalness: 0.8,
            roughness: 0.2
          });
          const disk = new THREE.Mesh(diskGeom, diskMat);
          disk.position.y = 0.6;
          charGroup.add(disk);

          // Glowing Thruster Ring
          const ringGeom = new THREE.TorusGeometry(2.9, 0.3, 8, 24);
          ringGeom.rotateX(Math.PI / 2);
          const ringMat = new THREE.MeshBasicMaterial({ color: color });
          const ring = new THREE.Mesh(ringGeom, ringMat);
          ring.position.y = 1.25;
          charGroup.add(ring);

          // 2. Character Body Assembly
          const bodyAssembly = new THREE.Group();
          bodyAssembly.position.y = 1.4;

          // Torso / Armor
          const torsoGeom = new THREE.BoxGeometry(2.4, 3.2, 1.8);
          const torsoMat = new THREE.MeshStandardMaterial({
            color: color,
            roughness: 0.35,
            metalness: 0.65
          });
          const torso = new THREE.Mesh(torsoGeom, torsoMat);
          torso.position.y = 1.6;
          torso.castShadow = true;
          bodyAssembly.add(torso);

          // Glowing Core Reactor Arc on Chest
          const reactorGeom = new THREE.CylinderGeometry(0.55, 0.55, 0.25, 12);
          reactorGeom.rotateX(Math.PI / 2);
          const reactorMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
          const reactor = new THREE.Mesh(reactorGeom, reactorMat);
          reactor.position.set(0, 1.8, 1.0);
          bodyAssembly.add(reactor);

          // Cybernetic Head
          const headGeom = new THREE.BoxGeometry(1.6, 1.6, 1.6);
          const headMat = new THREE.MeshStandardMaterial({
            color: 0xf1f5f9,
            metalness: 0.9,
            roughness: 0.15
          });
          const head = new THREE.Mesh(headGeom, headMat);
          head.position.y = 3.8;
          head.castShadow = true;
          bodyAssembly.add(head);

          // Glowing Visor
          const visorGeom = new THREE.BoxGeometry(1.3, 0.45, 0.3);
          const visorMat = new THREE.MeshBasicMaterial({ color: 0x00f3ff });
          const visor = new THREE.Mesh(visorGeom, visorMat);
          visor.position.set(0, 3.8, 0.85);
          bodyAssembly.add(visor);

          // Shoulders
          [-1.6, 1.6].forEach(sx => {
            const shoulder = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.8, 0.8), torsoMat);
            shoulder.position.set(sx, 2.6, 0);
            bodyAssembly.add(shoulder);

            const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.35, 0.35, 2.2, 8), headMat);
            arm.position.set(sx, 1.3, 0);
            bodyAssembly.add(arm);
          });

          // Special Tool/Accessory for Iconic Agents
          let itemMesh = null;
          if (agent.id === 'hadi-core') {
            itemMesh = new THREE.Mesh(new THREE.OctahedronGeometry(1.4, 0), new THREE.MeshBasicMaterial({ color: 0xf59e0b }));
            itemMesh.position.set(0, 5.4, 0);
            bodyAssembly.add(itemMesh);
          } else if (agent.id === 'hadi-maestro') {
            itemMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 3.6, 8), new THREE.MeshBasicMaterial({ color: 0x38bdf8 }));
            itemMesh.position.set(1.8, 2.6, 0.6);
            itemMesh.rotateZ(-Math.PI / 4);
            bodyAssembly.add(itemMesh);
          } else if (agent.id === 'sareem-security') {
            itemMesh = new THREE.Mesh(new THREE.BoxGeometry(0.3, 2.6, 1.8), new THREE.MeshStandardMaterial({ color: 0xef4444, metalness: 0.8 }));
            itemMesh.position.set(1.8, 2.8, 0.8);
            bodyAssembly.add(itemMesh);
          } else if (agent.id === 'sajeel-logger') {
            itemMesh = new THREE.Mesh(new THREE.PlaneGeometry(2, 3), new THREE.MeshBasicMaterial({ color: 0x60a5fa, side: THREE.DoubleSide, transparent: true, opacity: 0.8 }));
            itemMesh.position.set(1.8, 3.2, 1.2);
            itemMesh.rotateY(-Math.PI / 4);
            bodyAssembly.add(itemMesh);
          }

          charGroup.add(bodyAssembly);

          // Floating Title Sprite Label
          const sprite = createCharacterBillboardSprite(agent.emoji + ' ' + agent.name_ar, agent.emoji + ' ' + agent.name_en);
          sprite.position.y = 9.0;
          charGroup.add(sprite);

          charGroup.userData = {
            agentId: agent.id,
            agent: agent,
            division: div.id,
            bodyAssembly: bodyAssembly,
            torso: torso,
            head: head,
            ring: ring,
            homePosition: charGroup.position.clone(),
            sprite: sprite
          };

          scene.add(charGroup);
          characterAvatars.push(charGroup);
        });
      });
    }'''

pattern_agents = re.compile(r'function buildArticulatedAgentCharacters\(\) \{[\s\S]+?characterAvatars\.push\(charGroup\);\s*\}\);?\s*\}', re.MULTILINE)
assert pattern_agents.search(content), "Could not find buildArticulatedAgentCharacters pattern!"
content = pattern_agents.sub(replacement_agents_code, content)

# 3. Replacement for runKineticMissionSimulation (MULTI-AGENT SYNCHRONIZED SQUADRON FLIGHT)
replacement_sim_code = '''    async function runKineticMissionSimulation() {
      if (state.isSimulating) return;
      state.isSimulating = true;

      const isAr = state.lang === 'ar';
      const btn = document.getElementById('btn-run-sim');
      btn.disabled = true;
      btn.innerHTML = `<span>⏳</span> <span>${I18N[state.lang].simRunning}</span>`;

      const terminal = document.getElementById('terminal-box');
      terminal.innerHTML = '';

      const mission = MISSIONS[state.activeMissionIndex];

      function addLog(agentId, msg) {
        const ag = DATA.agents.find(a => a.id === agentId) || { emoji: '🤖', name_ar: agentId, name_en: agentId };
        const now = new Date();
        const timeStr = `${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
        const div = document.createElement('div');
        div.className = 'log-line';
        div.innerHTML = `
          <span class="log-time">[${timeStr}]</span>
          <span class="log-agent" style="color:var(--gold);">${ag.emoji} [${isAr ? ag.name_ar : ag.name_en}]:</span>
          <span class="log-msg">${msg}</span>
        `;
        terminal.appendChild(div);
        terminal.scrollTop = terminal.scrollHeight;
      }

      // Execute each step with synchronized multi-agent team squadron movement!
      for (let i = 0; i < mission.steps.length; i++) {
        const step = mission.steps[i];
        const agent = DATA.agents.find(a => a.id === step.agent);
        const char = characterAvatars.find(c => c.userData.agentId === step.agent);

        if (agent && char) {
          selectAgent(agent.id, false);

          const divId = char.userData.division || agent.division;
          const div = DATA.divisions.find(d => d.id === divId);

          // Fly camera to a panoramic view framing the whole island and its agents
          if (div) {
            const isSky = div.id === 'lead';
            const baseY = isSky ? 38 : div.coords.y;
            flyCameraTo(
              { x: div.coords.x + 48, y: baseY + 45, z: div.coords.z + 62 },
              { x: div.coords.x, y: baseY + 6, z: div.coords.z },
              1.3
            );
          }

          // COLLECT ALL AGENTS STATIONED ON THIS ACTIVE ISLAND (ALL TEAMMATES MOVE TOGETHER!)
          const islandTeammates = characterAvatars.filter(c => c.userData.division === divId);
          const isSky = div && div.id === 'lead';
          const islandTopY = (isSky ? 38 : (div ? div.coords.y : 6)) + ((div ? div.scale.y : 10) * 1.3 * 0.45);
          const centerX = div ? div.coords.x : char.userData.homePosition.x;
          const centerZ = div ? div.coords.z : char.userData.homePosition.z;

          // Lead agent flies to central command focus
          const leadTarget = new THREE.Vector3(centerX, islandTopY + 8.0, centerZ);

          // ALL teammates simultaneously launch into airborne tactical formation!
          const teamCount = islandTeammates.length;
          const formationRadius = 22;

          const teamLaunchAnimations = islandTeammates.map((teammate, tIdx) => {
            if (teammate === char) {
              return animateCharacterToTarget(char, leadTarget, 1.2);
            } else {
              const ang = (tIdx / teamCount) * Math.PI * 2;
              const teamTarget = new THREE.Vector3(
                centerX + Math.cos(ang) * formationRadius,
                islandTopY + 6.0 + ((tIdx % 3) * 1.8),
                centerZ + Math.sin(ang) * formationRadius
              );
              return animateCharacterToTarget(teammate, teamTarget, 1.1 + (tIdx * 0.06));
            }
          });

          await Promise.all(teamLaunchAnimations);

          // Coordinated collaborative excitation & full rotation
          islandTeammates.forEach((tm, idx) => {
            gsap.to(tm.userData.bodyAssembly.rotation, {
              y: Math.PI * 2,
              duration: 1.1,
              ease: 'power1.inOut'
            });
            gsap.to(tm.userData.torso.scale, {
              x: 1.35, y: 1.35, z: 1.35,
              yoyo: true,
              repeat: 1,
              duration: 0.55
            });
          });

          addLog(step.agent, isAr ? step.text_ar : step.text_en);
          await new Promise(r => setTimeout(r, 1600));

          // Return ENTIRE team smoothly back to their circular pedestals
          const teamReturns = islandTeammates.map(teammate => {
            return animateCharacterToTarget(teammate, teammate.userData.homePosition, 0.95);
          });
          await Promise.all(teamReturns);
          await new Promise(r => setTimeout(r, 350));
        } else {
          addLog(step.agent, isAr ? step.text_ar : step.text_en);
          await new Promise(r => setTimeout(r, 1200));
        }
      }

      addLog('hadi-core', I18N[state.lang].simDone);

      state.isSimulating = false;
      btn.disabled = false;
      btn.innerHTML = `<span>▶</span> <span>${I18N[state.lang].simRun}</span>`;
    }'''

pattern_sim = re.compile(r'async function runKineticMissionSimulation\(\) \{[\s\S]+?btn\.innerHTML = `<span>▶</span> <span>\$\{I18N\[state\.lang\]\.simRun\}</span>`;\s*\}', re.MULTILINE)
assert pattern_sim.search(content), "Could not find runKineticMissionSimulation pattern!"
content = pattern_sim.sub(replacement_sim_code, content)

# 4. Update overview camera preset
content = content.replace(
    "if (cam === 'overview') flyCameraTo({ x: 0, y: 160, z: 210 }, { x: 0, y: 8, z: 0 });",
    "if (cam === 'overview') flyCameraTo({ x: 0, y: 210, z: 270 }, { x: 0, y: 8, z: 0 });"
)
content = content.replace(
    "flyCameraTo({ x: 0, y: 160, z: 210 }, { x: 0, y: 8, z: 0 });",
    "flyCameraTo({ x: 0, y: 210, z: 270 }, { x: 0, y: 8, z: 0 });"
)

open(html_path, 'w', encoding='utf-8').write(content)
print("Successfully upgraded all islands, rich landmarks, and multi-agent synchronized squadron flight!")
