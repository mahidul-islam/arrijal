function makeInstance(geometry, color, x) {
	const material = new THREE.MeshPhongMaterial({color});
	const cube = new THREE.Mesh(geometry, material);
	scene.add(cube);
	cube.position.x = x;
	return cube;
}
