function drawEqual(root) {
  const x = 100;
  const y = 20;
  const z = 20;

  const equel = new THREE.Object3D()
  equel.scale.set(1,1,1)

  const equelGeometry = new THREE.BoxBufferGeometry(x ,y ,z);
  const equelMaterial = new THREE.MeshPhongMaterial({color: 0x008988})

  const equelUp = new THREE.Mesh(equelGeometry, equelMaterial)
  equelUp.position.y = 30

  const equelDown = new THREE.Mesh(equelGeometry, equelMaterial)
  equelDown.position.y = -30

  equel.add(equelUp)
  equel.add(equelDown)
  root.add(equel)
}
