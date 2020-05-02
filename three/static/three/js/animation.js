var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry(1,1,1);

function makeInstance(geometry, color, x) {
	const material = new THREE.MeshPhongMaterial({color});
	const cube = new THREE.Mesh(geometry, material);
	scene.add(cube);
	cube.position.x = x;
	return cube;
}

const cubes = [
	makeInstance(geometry, 0x44aa88, 0),
	makeInstance(geometry, 0x44aa88, -2),
	makeInstance(geometry, 0x44aa88, 2)
]

const color = 0xFFFFFF;
const intensity = 1;
const light = new THREE.DirectionalLight(color, intensity);
const light2 = new THREE.DirectionalLight(color, intensity);
const light3 = new THREE.DirectionalLight(color, intensity);
light.position.set(0, 8, 0);
light2.position.set(0, -8, 0);
light3.position.set(0, 0, 8);
scene.add(light, light2, light3);

camera.position.z = 5;

var animate = function () {
	requestAnimationFrame( animate );

	cubes[0].rotation.x += 0.01;
	cubes[1].rotation.y += 0.01;
	cubes[2].rotation.z += 0.01;

	renderer.render( scene, camera );
};
// console.log('working')

animate();
