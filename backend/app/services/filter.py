class Filter_my_data:
    
    def __init__(self):
        'filters the api output to neccesary data'
        pass

    def filter(self,data):
        '''
        input: api output
        output: json containing temperature_2m_max,temperature_2m_min and elevation 
        '''
        elevation = data['elevation']
        temperature_2m_max = data['daily']['temperature_2m_max']
        temperature_2m_min = data['daily']['temperature_2m_min']
        return {'temperature_2m_max':temperature_2m_max,
                "temperature_2m_min":temperature_2m_min,
                "elevation":elevation
                }


if __name__ == "__main__":
    data = ({'latitude': 52.52, 'longitude': 13.419998, 'generationtime_ms': 0.11932849884033203, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 38.0, 'daily_units': {'time': 'iso8601', 'temperature_2m_max': '�C', 'temperature_2m_min': '�C', 'sunrise': 'iso8601'}, 'daily': {'time': ['2026-02-14', '2026-02-15', '2026-02-16', '2026-02-17', '2026-02-18', '2026-02-19', '2026-02-20', '2026-02-21', '2026-02-22', '2026-02-23', '2026-02-24', '2026-02-25', '2026-02-26', '2026-02-27'], 'temperature_2m_max': [1.1, 0.3, -2.8, -0.4, -0.6, 0.1, 0.6, 9.2, 10.5, 8.6, 8.9, 16.2, 13.0, 12.5], 'temperature_2m_min': [-1.5, -3.9, -5.0, -4.0, -3.7, -6.8, -6.6, -0.4, 6.4, 5.5, 5.1, 6.8, 7.2, 9.0], 'sunrise': ['2026-02-14T06:24', '2026-02-15T06:22', '2026-02-16T06:20', '2026-02-17T06:18', '2026-02-18T06:16', '2026-02-19T06:14', '2026-02-20T06:12', '2026-02-21T06:09', '2026-02-22T06:07', '2026-02-23T06:05', '2026-02-24T06:03', '2026-02-25T06:01', '2026-02-26T05:59', '2026-02-27T05:56']}}, {'latitude': 52.52, 'longitude': 13.419998, 'generationtime_ms': 0.0699758529663086, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 38.0, 'daily_units': {'time': 'iso8601', 'temperature_2m_max': '�C', 'temperature_2m_min': '�C', 'sunrise': 'iso8601'}, 'daily': {'time': ['2026-02-21', '2026-02-22', '2026-02-23', '2026-02-24', '2026-02-25', '2026-02-26', '2026-02-27'], 'temperature_2m_max': [9.2, 10.5, 8.6, 8.9, 16.2, 13.0, 12.5], 'temperature_2m_min': [-0.4, 6.4, 5.5, 5.1, 6.8, 7.2, 9.0], 'sunrise': ['2026-02-21T06:09', '2026-02-22T06:07', '2026-02-23T06:05', '2026-02-24T06:03', '2026-02-25T06:01', '2026-02-26T05:59', '2026-02-27T05:56']}})
    obj = Filter_my_data(data=data)
