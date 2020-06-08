function text2dLoader(base, text2 = 'Not Provided', html , color = 'red') {
  var text = document.createElement( 'div' );
	text.className = 'label';
	text.textContent = text2;
	text.style.marginTop = '-1em';
	var Label = new CSS2DObject( text );
  if(html != "none"){
    Label.element.innerHTML = html
    // Label.element.style.
  }
	Label.position.set( 0, 0, 0 );
	base.add( Label );
  console.log(Label.element)

  const box = new THREE.BoxGeometry(80, 80, 10);
  const material1 = new THREE.MeshPhongMaterial({color: 0x002B3B})
  const material2 = new THREE.MeshPhongMaterial({color: 0xE1DBC0})
  const material3 = new THREE.MeshPhongMaterial({color: 0x478379})
  const button1 = new THREE.Mesh(box, material1)
  const button2 = new THREE.Mesh(box, material2)
  const button3 = new THREE.Mesh(box, material3)
  base.add(button1)
  base.add(button2)
  base.add(button3)
  button1.position.x = -150
  button2.position.x = -150
  button3.position.x = -150
  button1.position.y = -30
  button2.position.y = -130
  button3.position.y = -230
  button1.name = text2 + '1'
  button2.name = text2 + '2'
  button3.name = text2 + '3'
}
