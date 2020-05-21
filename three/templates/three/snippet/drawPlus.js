function drawPlus(root) {
  const x = 100;
  const y = 20;
  const z = 20;

  const a = 20;
  const b = 100;
  const c = 20;

  const plus = new THREE.Object3D()
  plus.scale.set(1,1,1)

  const plusGeometry = new THREE.BoxBufferGeometry(x ,y ,z);
  const plusGeometry2 = new THREE.BoxBufferGeometry(a ,b ,c);
  const plusMaterial = new THREE.MeshPhongMaterial({color: 0x008988})

  const plusH = new THREE.Mesh(plusGeometry, plusMaterial)
  const plusV = new THREE.Mesh(plusGeometry2, plusMaterial)

  plus.add(plusH)
  plus.add(plusV)
  root.add(plus)
}
