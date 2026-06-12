// ==========================================================================
// 1. Three.js Background Particle Setup
// ==========================================================================
function initBackgroundParticles() {
  const canvas = document.querySelector('#bg');
  if (!canvas) return;

  // Create Scene, Camera and Renderer
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  
  renderer.setPixelRatio(window.devicePixelRatio);
  renderer.setSize(window.innerWidth, window.innerHeight);
  camera.position.setZ(30);

  // Geometry configuration: Custom scattered space particles
  const particlesGeometry = new THREE.BufferGeometry();
  const particlesCount = 400;
  const posArray = new Float32Array(particlesCount * 3);

  for(let i=0; i < particlesCount * 3; i++) {
    posArray[i] = (Math.random() - 0.5) * 80;
  }
  particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

  // Particle styling: Electric/Neon blue points matching the design theme
  const particlesMaterial = new THREE.PointsMaterial({
    size: 0.15,
    color: 0x00d4ff,
    transparent: true,
    opacity: 0.7
  });

  const particleMesh = new THREE.Points(particlesGeometry, particlesMaterial);
  scene.add(particleMesh);

  // Animation Loop (gentle drift effect)
  function animate() {
    requestAnimationFrame(animate);
    particleMesh.rotation.y += 0.001;
    particleMesh.rotation.x += 0.0005;
    renderer.render(scene, camera);
  }
  animate();

  // Responsive Screen resizing adaptation
  window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
}

// ==========================================================================
// 2. Mobile Responsive Navigation Toggle Logic
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
  // Initialize Background Canvas
  initBackgroundParticles();

  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  const navOverlay = document.querySelector(".nav-overlay");

  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      menuToggle.classList.toggle("active");
      navLinks.classList.toggle("active");
      navOverlay?.classList.toggle("active");
    });

    // Close drawers on anchor click
    document.querySelectorAll(".nav-links a").forEach((link) => {
      link.addEventListener("click", () => {
        menuToggle.classList.remove("active");
        navLinks.classList.remove("active");
        navOverlay?.classList.remove("active");
      });
    });
  }

  // Close interface drawers when backdrop clicking
  if (navOverlay) {
    navOverlay.addEventListener("click", () => {
      menuToggle?.classList.remove("active");
      navLinks?.classList.remove("active");
      navOverlay.classList.remove("active");
    });
  }
});

// ==========================================================================
// 3. Smooth Scrolling Implementation
// ==========================================================================
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    const targetId = this.getAttribute("href");
    if(targetId === "#") return;
    
    const target = document.querySelector(targetId);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({
        behavior: "smooth",
      });
    }
  });
});

// ==========================================================================
// 4. Glassmorphism Scroll Header Threshold Effects
// ==========================================================================
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");
  if (!navbar) return;
  
  navbar.classList.toggle("scrolled", window.scrollY > 50);
});