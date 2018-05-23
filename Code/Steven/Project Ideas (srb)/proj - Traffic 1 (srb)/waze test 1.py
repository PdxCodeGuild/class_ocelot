import WazeRouteCalculator

from_address = '608 Northwest 70th Circle, Vancouver, WA'
to_address = 'Southwest Corbett Avenue, Portland, OR'
region = 'US'
route = WazeRouteCalculator.WazeRouteCalculator(from_address, to_address, region)
route.calc_route_info()
