usage_module_info() { echo "Usage: $0 -d <Run Docker> -h <Run with monitor> -a <launch API calls> -r <Generate reports>" 1>&2; exit 1; }

while getopts ":dhar" o; do
    case "${o}" in
        d)
            RUN_DOCKER=1;;
        h)
            RUN_MONITOR=1;;
        a)
            RUN_ALL=1;;
        r)
            REPORT=1;;
        *)
            usage_module_info;;
    esac
done

shift $((OPTIND-1))

function run_docker() {
    docker-compose up --build fast-api
}


function run_monitor() {
#    docker-compose --compatibility up --build -d apis-container
    docker-compose --compatibility up --build fast-api
#    docker exec -it `docker ps -q --filter name=apis-container` bash -c "htop"
}

function run_all() {
  echo "Execute the next commands in different consoles"
  echo "sh profile.hs -h"
  echo "sh profile.hs -r"
  echo "artillery run dataFlow.yaml\n"
}

function generate_report() {
  echo "GETTING STATS..."
  while true; do docker stats -a --no-stream >> stats.txt; done
#  IF YOU WANT GET THE STATS AFTER DELAY UNCOMMENT THE NEXT LINE AND COMMENT THE ABOVE
#  while true; do docker stats --no-stream | tee --append stats_1-15.txt; sleep 1; done
};

echo

if [[ RUN_ALL -eq 1 ]]; then
  run_all
elif [[ $RUN_DOCKER -eq 1 ]]; then
  run_docker
elif [[ $RUN_MONITOR -eq 1 ]]; then
  run_monitor
elif [[ REPORT -eq 1 ]]; then
  generate_report
else
  usage_module_info;
fi
