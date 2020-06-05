function text2dLoader(base, text2 = 'Not Provided', color = 'red') {
  var text = document.createElement( 'div' );
	text.className = 'label';
	text.textContent = text2;
	text.style.marginTop = '-1em';
	var Label = new CSS2DObject( text );
	Label.position.set( 0, 0, 0 );
	base.add( Label );
}
