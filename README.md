# GWML
GWML artefacts - temporary repo to work on GWML schemas, schemas, etc.


Those artefact are meant to be transfer to Open Geospatial Consortium (http://schemas.opengis.net/gwml/) where official versions are available.

## Oasis catalog
In the schemas folder, there is a OASIS catalog.xml file that rewrites OGC URL to local resources.

```
    <rewriteURI
        uriStartString="http://schemas.opengis.net/gwml/2.2/"
        rewritePrefix="./" />
```

You can set your validator to use local schemas files instead of schemas from OGC server.

