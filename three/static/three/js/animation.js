// import * as LIB from './another.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight, false );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.BoxGeometry(1,1,1);
const loader = new THREE.TextureLoader();

function makeInstance(geometry, loader, color, x) {
	const material = new THREE.MeshPhongMaterial({color});
	const cube = new THREE.Mesh(geometry, material);
	scene.add(cube);
	cube.position.x = x;
	return cube;
}

const cubes = [
	makeInstance(geometry, loader, 0x44aa88, 2),
  makeInstance(geometry, loader, 0x009944, 0),
	makeInstance(geometry, loader, 0x44ff00, -2),
]

const color = 0xFFFFFF;
const intensity = 1;
const light = new THREE.DirectionalLight(color, intensity);
const light2 = new THREE.DirectionalLight(color, intensity);
const light3 = new THREE.DirectionalLight(color, intensity);
light.position.set(0, 8, 0);
light2.position.set(0, -8, 0);
light3.position.set(-4, 0, 8);
scene.add(light, light2, light3);

camera.position.z = 8;

const radius =  1;
const detail = 1;
const geometrys = new THREE.DodecahedronBufferGeometry(radius, detail);

const material = new THREE.MeshPhongMaterial({color:0xcc1122});
const sphere = new THREE.Mesh(geometrys, material);
sphere.position.y = 3;
scene.add(sphere);


let animate = function () {
	requestAnimationFrame( animate );

	cubes[0].rotation.x += 0.01;
	cubes[1].rotation.y += 0.01;
	cubes[2].rotation.z += 0.01;
	sphere.rotation.x += 0.1;
	renderer.render( scene, camera );
};
// console.log('working')

animate();
