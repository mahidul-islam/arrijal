function text2dLoader(base, text2 = 'Not Provided', html , color = 'red') {
  var text = document.createElement( 'div' );
	text.className = 'label';
	text.textContent = text2;
	text.style.marginTop = '-1em';
	var Label = new CSS2DObject( text );
  if(html != "none"){
    Label.element.innerHTML = html
  }
	Label.position.set( 0, 0, 0 );
  Label.name = text2
	base.add( Label );
  // console.log(Label.element.innerHTML)
}
