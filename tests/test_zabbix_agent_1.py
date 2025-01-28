import subprocess
import pytest

@pytest.fixture
def zabbix_agent1_output():
    keys = [
        "postfix.version",
        "postfix.startup",
        "net.tcp.port[,25]",
        "mailq-total",
        "mailq-count[active]",
        "mailq-count[deferred]",
        "mailq-count[hold]",
        "mailq-count[bounce]"
    ]
    results = {}
    for key in keys:
        output = subprocess.check_output(["zabbix_get", "-s", "127.0.0.1", "-p", "10051", "-k", key]).decode("utf-8").strip()
        results[key] = output
    return results

def test_zabbix_agent1(zabbix_agent1_output):
    for key, output in zabbix_agent1_output.items():
        assert output is not None, f"Output for {key} should not be None"
        assert output != "", f"Output for {key} should not be an empty string"
        
        # Type checks based on expected output
        if key == "postfix.version":
            assert isinstance(output, str) and output.count('.') == 2, f"Expected version string for {key}, got: {output}"
        elif key == "postfix.startup":
            assert output in ["enabled", "disabled"], f"Expected 'enabled' or 'disabled' for {key}, got: {output}"
        elif key in ["net.tcp.port[,25]", "mailq-total", "mailq-count[active]", "mailq-count[deferred]", "mailq-count[hold]", "mailq-count[bounce]"]:
            assert output.isdigit(), f"Expected digit string for {key}, got: {output}"

