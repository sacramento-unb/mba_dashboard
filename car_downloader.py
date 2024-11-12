import requests
import geopandas as gpd
from io import BytesIO

def baixar_car(cod_imovel):
    state = cod_imovel.lower()[0:2]

    url = 'https://geoserver.car.gov.br/geoserver/sicar/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=sicar:sicar_imoveis_'+state+'&outputFormat=application/json&cql_filter=cod_imovel='+'\''+cod_imovel+'\''
    print(url)

    r = requests.get(url,allow_redirects=True,verify=False)

    gdf = gpd.read_file(BytesIO(r.content))

    return gdf


if __name__ == '__main__':  
    baixar_car('GO-5207808-883FE12618254568859AD7A3C87719EC')
