#compdef clab

function get_envs()
{
    env_string=$(ls /anaconda/envs/)
    env_list=$(echo $env_string | tr " " "\n")
}

_clab() {
  local state

  _arguments \
    '1: :->envs'
  get_envs
  case $state in
	  (envs) _arguments "1:profiles:($env_string)" ;;
  esac
}

_clab "$@"
