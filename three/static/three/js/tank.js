import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r115/build/three.module.js';
import {GUI} from 'https://threejsfundamentals.org/threejs/../3rdparty/dat.gui.module.js';

function main() {

  const canvas = document.querySelector('#c');
  const renderer = new THREE.WebGLRenderer({canvas});
  const gui = new GUI();

  const fov = 40;
  const aspect = 2;  // the canvas default
  const near = 0.1;
  const far = 1000;
  const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
  camera.position.set(0, 50, 0);
  camera.up.set(0, 0, 1);
  camera.lookAt(0, 0, 0);

  const scene = new THREE.Scene();

  {
    const color = 0xFFFFFF;
    const intensity = 3;
    const light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(20, 50, 20)
    scene.add(light);
  }

  const objects = [];

  const radius = 1;
  const widthSegments = 10;
  const heightSegments = 10;
  const sphereGeometry = new THREE.SphereBufferGeometry(radius, widthSegments, heightSegments);

  const ao = new THREE.Object3D();
  scene.add(ao)
  objects.push(ao)

  const bo = new THREE.Object3D()
  ao.add(bo)
  objects.push(bo)
  bo.position.x = 10

  const co = new THREE.Object3D()
  bo.add(co)
  objects.push(co)
  co.position.x = 2

  const am = new THREE.MeshPhongMaterial({color: 0x898988})
  const amesh = new THREE.Mesh(sphereGeometry, am)
  amesh.scale.set(5,5,5)
  ao.add(amesh)

  const bm = new THREE.MeshPhongMaterial({color: 0x890000})
  const bmesh = new THREE.Mesh(sphereGeometry, bm)
  bmesh.scale.set(1,1,1)
  bo.add(bmesh)

  const cm = new THREE.MeshPhongMaterial({color: 0x008988})
  const cmesh = new THREE.Mesh(sphereGeometry, cm)
  cmesh.scale.set(2,2,2)
  co.add(cmesh)

  class AxisGridHelper {
      constructor(node, units = 10) {
        const axes = new THREE.AxesHelper();
        axes.material.depthTest = false;
        axes.renderOrder = 2;  // after the grid
        node.add(axes);

        const grid = new THREE.GridHelper(units, units);
        grid.material.depthTest = false;
        grid.renderOrder = 1;
        node.add(grid);

        this.grid = grid;
        this.axes = axes;
        this.visible = false;
      }
      get visible() {
        return this._visible;
      }
      set visible(v) {
        this._visible = v;
        this.grid.visible = v;
        this.axes.visible = v;
      }
    }

    function makeAxisGrid(node, label, units) {
      const helper = new AxisGridHelper(node, units);
      gui.add(helper, 'visible').name(label);
    }

    makeAxisGrid(ao, 'solarSystem', 26);
    makeAxisGrid(amesh, 'sunMesh');
    makeAxisGrid(bo, 'earthOrbit');
    makeAxisGrid(bmesh, 'earthMesh');
    makeAxisGrid(cmesh, 'moonMesh');

  function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
      renderer.setSize(width, height, false);
    }
    return needResize;
  }

  function render(time) {
    time *= 0.001;

    if (resizeRendererToDisplaySize(renderer)) {
      const canvas = renderer.domElement;
      camera.aspect = canvas.clientWidth / canvas.clientHeight;
      camera.updateProjectionMatrix();
    }

    objects.forEach((obj) => {
      obj.rotation.y = time;
    });

    renderer.render(scene, camera);

    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
}

main();
