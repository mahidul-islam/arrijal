function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();

  renderer.setSize( window.innerWidth, window.innerHeight );
  labelRenderer.setSize( window.innerWidth, window.innerHeight );

  render();
}

function animate() {
  requestAnimationFrame( animate );
  controls.update();

  var time = Date.now() * 0.0004;

  if(rotatate == true){
    objects.forEach((obj) => {
      obj.rotation.x = time * 2;
      obj.rotation.y = time * 0.7 * 2;
    });
    objects2.forEach((obj) => {
      obj.rotation.y = time * 2;
      obj.rotation.z = time * 0.7 * 2;
    });
    objects3.forEach((obj) => {
      obj.rotation.x = time * 2;
      obj.rotation.z = time * 0.7 * 2;
    });
  }

  render();
}

function render() {
  renderer.render( scene, camera );
  labelRenderer.render( scene, camera );
}
