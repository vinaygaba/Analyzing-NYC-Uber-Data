#Map Data Binding
import json
import pandas as pd
import vincent
#Map the county codes we have in our geometry to those in the
#county_data file, which contains additional rows we don't need
with open('us_counties.topo.json', 'r') as f:
    get_id = json.load(f)

#A little FIPS code munging
new_geoms = []
for geom in get_id['objects']['us_counties.geo']['geometries']:
    geom['properties']['FIPS'] = int(geom['properties']['FIPS'])
    new_geoms.append(geom)

get_id['objects']['us_counties.geo']['geometries'] = new_geoms

with open('us_counties.topo.json', 'w') as f:
    json.dump(get_id, f)

#Grab the FIPS codes and load them into a dataframe
geometries = get_id['objects']['us_counties.geo']['geometries']
county_codes = [x['properties']['FIPS'] for x in geometries]
county_df = pd.DataFrame({'FIPS': county_codes}, dtype=str)
county_df = county_df.astype(int)

#Read into Dataframe, cast to string for consistency
df = pd.read_csv('us_county_data.csv', na_values=[' '])
df['FIPS_Code'] = df['FIPS'].astype(str)

#Perform an inner join, pad NA's with data from nearest county
merged = pd.merge(df, county_df, on='FIPS', how='inner')
merged = merged.fillna(method='pad')

#'merged' is the Pandas DataFrame
vis = vincent.Map(width=1000, height=800)
vis.tabular_data(merged, columns=['FIPS_Code', 'Unemployment_rate_2011'])
vis.geo_data(projection='albersUsa', scale=1000, bind_data='data.id', counties=county_geo)
vis + (["#f5f5f5","#000045"], 'scales', 0, 'range')
vis.to_json(path)
