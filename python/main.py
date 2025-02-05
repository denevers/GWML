import xmlschema
from xmlschema import XsdElement


print("""
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .      
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix gwml2: <http://www.opengis.net/gwml-main/2.2> .
@prefix gml: <http://www.opengis.net/gml/3.2> .
@prefix swe: <http://www.opengis.net/swe/2.0> .
@prefix gwml2f: <http://www.opengis.net/gwml-flow/2.2> .
@prefix gwml2c: <http://www.opengis.net/gwml-constituent/2.2> .
@prefix gco: <http://www.isotc211.org/2005/gco> .
@prefix gsml: <http://www.opengis.net/gsml/4.1/GeoSciML-Basic> .
@prefix om: <http://www.opengis.net/om/2.0> .
@prefix gmd: <http://www.isotc211.org/2005/gmd> .
@prefix gwml2wc: <http://www.opengis.net/gwml-wellconstruction/2.2> .
@prefix gwml2w: <http://www.opengis.net/gwml-well/2.2> .

      """
      )

replacement = str.maketrans({"{":"","}":""})

def dump_ttl(schema_location):
    gwml = xmlschema.XMLSchema(schema_location)
    for xsd_component in gwml.iter_components():
        if isinstance(xsd_component,XsdElement):
            print(f"{xsd_component.prefixed_name} a owl:Class.")
            xsdtype = xsd_component.substitution_group
            if xsdtype is not None:
                parent_name = xsdtype.translate(replacement)
                print(f"{xsd_component.prefixed_name} rdfs:subClassOf <{parent_name}>.")



dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-main.xsd")
dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-aquifertest.xsd")
dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-constituent.xsd")
dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-flow.xsd")
dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-well.xsd")
dump_ttl("https://schemas.opengis.net/gwml/2.2/gwml2-wellconstruction.xsd")