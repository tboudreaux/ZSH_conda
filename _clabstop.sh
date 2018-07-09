#compdef clabstop

function get_running_envs()
{
    running=$(running_labs)
}

_clabstop() {
  local state

  _arguments \
    '1: :->envs'
  get_running_envs
  case $state in
	  (envs) _arguments "1:profiles:($running)" ;;
  esac
}

_clabstop "$@"
