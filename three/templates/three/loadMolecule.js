function loadMolecule( url, root, text='not given' ) {
  while ( root.children.length > 0 ) {

    var object = root.children[ 0 ];
    object.parent.remove( object );
  }

  const rotatingObject = new THREE.Object3D()
  const stationaryObject = new THREE.Object3D()
  root.add(rotatingObject)
  root.add(stationaryObject)
  objects.push(rotatingObject)

  {% include 'three/textLoader.js' %}
  stationaryObject.position.y = 150
  stationaryObject.position.x = -150
  textLoader(stationaryObject, text)

  loader.load( url, function ( pdb ) {

    var geometryAtoms = pdb.geometryAtoms;
    var geometryBonds = pdb.geometryBonds;
    var json = pdb.json;

    var boxGeometry = new THREE.BoxBufferGeometry( 1, 1, 1 );
    var sphereGeometry = new THREE.IcosahedronBufferGeometry( 1, 2 );

    geometryAtoms.computeBoundingBox();
    geometryAtoms.boundingBox.getCenter( offset ).negate();
    console.log(geometryAtoms.boundingBox)

    geometryAtoms.translate( offset.x, offset.y, offset.z );
    geometryBonds.translate( offset.x, offset.y, offset.z );

    var positions = geometryAtoms.getAttribute( 'position' );
    var colors = geometryAtoms.getAttribute( 'color' );

    var position = new THREE.Vector3();
    var color = new THREE.Color();

    for ( var i = 0; i < positions.count; i ++ ) {

      position.x = positions.getX( i );
      position.y = positions.getY( i );
      position.z = positions.getZ( i );

      color.r = colors.getX( i );
      color.g = colors.getY( i );
      color.b = colors.getZ( i );

      var atom = json.atoms[ i ];

      var text = document.createElement( 'div' );
      text.className = 'label';
      text.style.color = 'rgb(' + atom[ 3 ][ 0 ] + ',' + atom[ 3 ][ 1 ] + ',' + atom[ 3 ][ 2 ] + ')';
      text.textContent = atom[ 4 ];

      {% include 'three/changeColor.js' %}

      var material = new THREE.MeshPhongMaterial( { color: color } );

      var object = new THREE.Mesh( sphereGeometry, material );
      object.position.copy( position );
      object.position.multiplyScalar( 75 );
      object.scale.multiplyScalar( 25 );
      rotatingObject.add( object );

      var label = new CSS2DObject( text );
      label.position.copy( object.position );
      rotatingObject.add( label );
    }

    positions = geometryBonds.getAttribute( 'position' );

    var start = new THREE.Vector3();
    var end = new THREE.Vector3();

    for ( var i = 0; i < positions.count; i += 2 ) {

      start.x = positions.getX( i );
      start.y = positions.getY( i );
      start.z = positions.getZ( i );

      end.x = positions.getX( i + 1 );
      end.y = positions.getY( i + 1 );
      end.z = positions.getZ( i + 1 );

      start.multiplyScalar( 75 );
      end.multiplyScalar( 75 );

      var object = new THREE.Mesh( boxGeometry, new THREE.MeshPhongMaterial( 0xffffff ) );
      object.position.copy( start );
      object.position.lerp( end, 0.5 );
      object.scale.set( 5, 5, start.distanceTo( end ) );
      object.lookAt( end );
      rotatingObject.add( object );
    }
    render();
  } );
}
