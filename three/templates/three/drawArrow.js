function drawArrow(mol1, mol2) {
  const to = new THREE.Vector3();
  mol2.getWorldPosition(to);
  const from = new THREE.Vector3();
  mol1.getWorldPosition(from);
  const direction = to.clone().sub(from);
  // const radious =
  const length = direction.length();
  const hex = 0x00AA00;
  const arrow = new THREE.ArrowHelper( direction.normalize(), from, length, hex );
  scene.add( arrow );
}
