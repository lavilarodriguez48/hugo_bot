def generar_xml(preguntas):
    xml = '<quiz>\n'
    for p in preguntas:
        xml += f'''
  <question type="multichoice">
    <name><text>{p["pregunta"]}</text></name>
    <questiontext format="html"><text><![CDATA[{p["pregunta"]}]]></text></questiontext>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>
'''
        for opcion in p["opciones"]:
            correcta = "100" if opcion == p["correcta"] else "0"
            xml += f'''
    <answer fraction="{correcta}">
      <text><![CDATA[{opcion}]]></text>
    </answer>
'''
        xml += "  </question>\n"
    xml += "</quiz>"
    return xml
