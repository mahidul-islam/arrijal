function loadEquation( base, equation, distance, initial){
  let position = initial;

  for(let i=0; i<equation.ingredients.length; i++){
    const root = new THREE.Group()
    root.position.x = position
    position += distanceBetweenMol
    base.add( root )
    loadMolecule( equation.ingredients[i].url, root, equation.ingredients[i].name );
    // console.log(equation.ingredients[0].url)

    if(equation.ingredients[i+1]){
      const root2 = new THREE.Group()
      root2.position.x = position
      position += distanceBetweenMol
      base.add( root2 )
      drawPlus(root2);
    }
  }

  const root = new THREE.Group()
  root.position.x = position
  position += distanceBetweenMol
  base.add( root )
  drawEqual(root)

  for(let i=0; i<equation.results.length; i++){
    const root = new THREE.Group()
    root.position.x = position
    position += distanceBetweenMol
    base.add( root )
    loadMolecule( equation.results[i].url, root, equation.results[i].name );

    if(equation.results[i+1]){
      const root2 = new THREE.Group()
      root2.position.x = position
      position += distanceBetweenMol
      base.add( root2 )
      drawPlus(root2);
    }
  }
}
