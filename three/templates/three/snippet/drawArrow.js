function drawArrow(mol1, mol2) {
  const to = new THREE.Vector3()
  mol2.getWorldPosition(to)
  const from = new THREE.Vector3()
  mol1.getWorldPosition(from)
  const direction = to.clone().sub(from)
  // const radious =
  const length = direction.length() - 200
  const arrowHeadL = 150
  const arrowHeadW = 40
  const hex = 0x222222;
  const arrow = new THREE.ArrowHelper( direction.normalize(), from, length, hex, arrowHeadL, arrowHeadW );
  scene.add( arrow )
  return arrow
}
