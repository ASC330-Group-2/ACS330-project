#All the active assets in the factory will send status update messages periodically, with a period #of 5 seconds to begin with.  This information is required for the CMS to track production and #generate relevant AMR Tasks.
#The main status indicates the condition of the asset in question, and assets with two conveyors #have additional statuses.

string asset_id
int8 status_main
int8 status_conveyor1
int8 status_conveyor2
