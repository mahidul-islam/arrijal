function init(position, toAdd) {

  scene = new THREE.Scene();
  scene.background = new THREE.Color( 0xFEF1D2 );

  camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 1, 5000 );
  camera.position.z = position.position.z;
  scene.add( camera );

  var light = new THREE.DirectionalLight( 0xffffff, 0.8 );
  light.position.set( 1, 1, 1 );
  scene.add( light );

  var light = new THREE.DirectionalLight( 0xffffff, 0.5 );
  light.position.set( - 1, - 1, 1 );
  scene.add( light );

  var light = new THREE.DirectionalLight( 0xffffff, 0.2 );
  light.position.set( 0, 0, 1000 );
  scene.add( light );

  var light = new THREE.DirectionalLight( 0xffffff, 0.2 );
  light.position.set( 0, 0, -1000 );
  scene.add( light );

//  var light = new THREE.DirectionalLight( 0xffffff, 0.2 );
//  light.position.set( 0, 0, 1000 );
//  scene.add( light );

  renderer = new THREE.WebGLRenderer( { antialias: true } );
  renderer.setPixelRatio( window.devicePixelRatio );
  renderer.setSize( window.innerWidth, window.innerHeight );
  document.getElementById( 'container' ).appendChild( renderer.domElement );

  labelRenderer = new CSS2DRenderer();
  labelRenderer.setSize( window.innerWidth, window.innerHeight );
  labelRenderer.domElement.style.position = 'absolute';
  labelRenderer.domElement.style.top = '0px';
  labelRenderer.domElement.style.pointerEvents = 'none';
  document.getElementById( 'container' ).appendChild( labelRenderer.domElement );

  controls = new TrackballControls( camera, renderer.domElement );
  controls.minDistance = 200;
  controls.maxDistance = 4000;

  window.addEventListener( 'resize', onWindowResize, false );


  const cbutton = document.createElement( 'button' );
  cbutton.innerHTML = "Initial Camera";
  toAdd.appendChild( cbutton );
  cbutton.addEventListener( 'click', cgenerateButtonCallback(  ), false );

  function cgenerateButtonCallback( url ) {
  	return function () {
  		movecamera( url );
  	};
  }
  function movecamera( url ) {
    controls.reset()
  }
}
