function drawAllMolsAndLinks(mol, root) {

  for (let i=0;i<mol.molecules.length;i++){
    const url = mol.molecules[i].url
    const name = mol.molecules[i].name
    let html = "none"
    if(mol.molecules[i].html){
      html = mol.molecules[i].html
    }
    const place = new THREE.Group()
    root.add(place)
    place.position.x = mol.molecules[i].positionX
    place.position.y = mol.molecules[i].positionY
    place.position.z = mol.molecules[i].positionZ
    loadMolecule( url, place, name, showLabel, html )
    if(i == 0)
      testmol = place.clone() 
  }

  // draw the links between molecules
  for (let i=0;i<mol.links.length;i++){
    const fromMol = mol.links[i].from
    const toMol = mol.links[i].to
    const placeFrom = new THREE.Group()
    const placeTo = new THREE.Group()

    for (let i=0;i<mol.molecules.length;i++){
      if(mol.molecules[i].name == fromMol){
        placeFrom.position.x = mol.molecules[i].positionX
        placeFrom.position.y = mol.molecules[i].positionY
        placeFrom.position.z = mol.molecules[i].positionZ
      }
      if(mol.molecules[i].name == toMol){
        placeTo.position.x = mol.molecules[i].positionX
        placeTo.position.y = mol.molecules[i].positionY
        placeTo.position.z = mol.molecules[i].positionZ
      }
    }
    drawArrow(placeFrom, placeTo)
  }
}
