function text3dLoader(base, text = 'Not Provided', color = 'red', size = 40){
  const loader = new THREE.FontLoader();
  // promisify font loading
  function loadFont(url) {
    return new Promise((resolve, reject) => {
      loader.load(url, resolve, undefined, reject);
    });
  }
  async function doit() {
      const font = await loadFont('https://threejsfundamentals.org/threejs/resources/threejs/fonts/helvetiker_regular.typeface.json');
      const geometry = new THREE.TextBufferGeometry(text, {
      font: font,
      size:  size,
      height:  10,
      curveSegments: 11,
      bevelEnabled: false,
      bevelThickness: 0.34,
      bevelSize: 0.48,
      bevelSegments: 8,
    });
    const material = new THREE.MeshPhongMaterial({color : color});
    const tmesh = new THREE.Mesh(geometry, material);
    base.add(tmesh);
  }
  doit();
}
