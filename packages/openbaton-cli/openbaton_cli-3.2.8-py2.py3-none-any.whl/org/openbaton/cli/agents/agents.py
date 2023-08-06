from __future__ import print_function

import json
import os

from org.openbaton.cli.errors.errors import WrongParameters
from org.openbaton.cli.utils.RestClient import RestClient


class BaseAgent(object):
    def __init__(self, client, url, project_id=None):
        self._client = client
        self.url = url
        if project_id is not None:
            self._client.project_id = project_id

    def find(self, _id=""):
        return self._client.get(self.url + "/%s" % _id)

    def delete(self, _id):
        self._client.delete(self.url + "/%s" % _id)

    def update(self, _id, entity):
        entity = entity.strip()
        if entity.endswith("}") or entity.endswith("]"):
            return json.loads(self._client.put(self.url + "/%s" % _id, json.dumps(json.loads(entity))))
        else:
            with open(entity) as f:
                return json.loads(self._client.put(self.url + "/%s" % _id, json.dumps(f.read().replace('\n', ''))))

    def create(self, entity='{}', _id=""):
        entity = entity.strip()
        if entity.endswith("}") or entity.endswith("]"):
            result = json.loads(self._client.post(self.url + "/%s" % _id, json.dumps(json.loads(entity))))
            return result
        else:
            if not os.path.isfile(entity):
                raise WrongParameters("%s is not a file")
            with open(entity) as f:
                file_content = f.read().replace('\n', '')
                return json.loads(self._client.post(self.url + "/%s" % _id, json.dumps(json.loads(file_content))))


class ProjectAgent(BaseAgent):
    def __init__(self, client):
        super(ProjectAgent, self).__init__(client, "projects")


class EventAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(EventAgent, self).__init__(client, "events", project_id=project_id)


class VimInstanceAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(VimInstanceAgent, self).__init__(client, "datacenters", project_id=project_id)

    def refresh(self, _id):
        self._client.get(self.url + "/%s/refresh" % _id)


class NSRAgent(BaseAgent):
    def create(self, entity='', _id="{}"):
        entity = entity.strip()
        return json.loads(self._client.post(self.url + "/%s" % entity, json.dumps(json.loads(_id))))

    def __init__(self, client, project_id):
        super(NSRAgent, self).__init__(client, "ns-records", project_id=project_id)


class KeyAgent(BaseAgent):
    def create(self, entity='', _id=None):
        if os.path.exists(entity) and os.path.isfile(entity):  # import
            with open(entity, 'r') as f:
                entity = f.read().replace('\n', '')

        entity = entity.strip()
        if entity.endswith("}") or entity.endswith("]"):
            result = json.loads(self._client.post(self.url, json.dumps(json.loads(entity))))
            return result
        else:  # generate
            key = self._client.post("%s/%s" % (self.url, 'generate'), entity)
        return key

    def __init__(self, client, project_id):
        super(KeyAgent, self).__init__(client, "keys", project_id=project_id)


class UserAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(UserAgent, self).__init__(client, "users", project_id=project_id)


class MarketAgent(BaseAgent):
    def update(self, _id, entity):
        raise WrongParameters('Market agent is allowed only to execute "create" passing a link')

    def delete(self, _id):
        raise WrongParameters('Market agent is allowed only to execute "create" passing a link')

    def find(self, _id=""):
        raise WrongParameters('Market agent is allowed only to execute "create" passing a link')

    def create(self, entity, _id="{}"):
        # entity will be the link
        entity = entity.strip()
        entity = {
            "link": entity
        }
        return json.loads(self._client.post(self.url, json.dumps(entity)))

    def __init__(self, client, project_id):
        super(MarketAgent, self).__init__(client, "ns-descriptors/marketdownload", project_id=project_id)


class LogAgent(BaseAgent):
    def update(self, _id, entity):
        raise WrongParameters('Market agent is allowed only to execute "show" passing: nsr_id, vnfr_name, hostname')

    def delete(self, _id):
        raise WrongParameters('Market agent is allowed only to execute "show" passing: nsr_id, vnfr_name, hostname')

    def find(self, nsr_id=None, vnfr_name=None, hostname=None, lines=None):
        if not vnfr_name or not hostname or not nsr_id:
            raise WrongParameters('LogAgent "show" method requires nsr_id, vnfr_name and hostname')
        if lines:
            body = json.dumps({'lines': int(lines)})
        else:
            body = None
        return self._client.post(self.url + "/%s/vnfrecord/%s/hostname/%s" % (nsr_id, vnfr_name, hostname), body)

    def create(self, entity, _id="{}"):
        raise WrongParameters('Market agent is allowed only to execute "show" passing: nsr_id, vnfr_name, hostname')

    def __init__(self, client, project_id):
        super(LogAgent, self).__init__(client, "logs", project_id=project_id)


class NSDAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(NSDAgent, self).__init__(client, "ns-descriptors", project_id=project_id)


class VNFPackageAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(VNFPackageAgent, self).__init__(client, "vnf-packages", project_id=project_id)

    def create(self, entity='', _id=""):
        if os.path.exists(entity) and os.path.isfile(entity) and entity.endswith(".tar"):
            return json.loads(self._client.post_file(self.url + "/%s" % _id, open(entity, "rb")))


class CSARNSDAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(CSARNSDAgent, self).__init__(client, "csar-nsd", project_id=project_id)

    def create(self, entity='', _id=""):
        if os.path.exists(entity) and os.path.isfile(entity) and entity.endswith(".csar"):
            return json.loads(self._client.post_file(self.url + "/%s" % _id, open(entity, "rb")))
        else:  # it is not a .csar file but a marketplace link
            return json.loads(self._client.post(self.url[:-1] + "/marketdownload/%s" % _id, '{"link":"%s"}' % entity))

    def update(self, _id, entity):
        raise WrongParameters('csarnsd agent is only allowed to execute "create"')

    def delete(self, _id):
        raise WrongParameters('csarnsd agent is only allowed to execute "create"')

    def find(self, _id=""):
        raise WrongParameters('csarnsd agent is only allowed to execute "create"')


class CSARVNFDAgent(BaseAgent):
    def __init__(self, client, project_id):
        super(CSARVNFDAgent, self).__init__(client, "csar-vnfd", project_id=project_id)

    def create(self, entity='', _id=""):
        if os.path.exists(entity) and os.path.isfile(entity) and entity.endswith(".csar"):
            return json.loads(self._client.post_file(self.url + "/%s" % _id, open(entity, "rb")))
        else:  # it is not a .csar file but a marketplace link
            return json.loads(self._client.post(self.url[:-1] + "/marketdownload/%s" % _id, '{"link":"%s"}' % entity))

    def update(self, _id, entity):
        raise WrongParameters('csarvnfd agent is only allowed to execute "create"')

    def delete(self, _id):
        raise WrongParameters('Market agent is only allowed to execute "create"')

    def find(self, _id=""):
        raise WrongParameters('Market agent is only allowed to execute "create"')


class SubAgent(BaseAgent):
    def __init__(self, client, project_id, main_agent, sub_url, sub_obj):
        super(SubAgent, self).__init__(client, sub_url, project_id=project_id)
        self.sub_obj = sub_obj
        self._main_agent = main_agent

    def update(self, _id, entity):
        nsd_id = self.__get_sub_obj_id_from_id__(_id)
        return super(SubAgent, self).update(nsd_id + "/" + self.sub_url + "/" + _id, entity)

    def find(self, _id=""):
        if _id is None or _id == "":
            raise WrongParameters("Please provide the id, only action show is allowed on this agent")
        nsd_id = self.__get_sub_obj_id_from_id__(_id)
        return self._main_agent.find(nsd_id + "/" + self.url + "/" + _id)

    def delete(self, _id):
        nsd_id = self.__get_sub_obj_id_from_id__(_id)
        super(SubAgent, self).delete(nsd_id + "/" + self.sub_url + "/" + _id)

    def create(self, entity='', _id=""):
        if _id is None or _id == "":
            raise WrongParameters("Please provide the id  of the object where to create this entity")
        return super(SubAgent, self).create(entity, _id + "/" + self.sub_url + "/")

    def __get_sub_obj_id_from_id__(self, _id):
        for obj in json.loads(self._main_agent.find()):
            for sub_obj in obj.get(self.sub_obj):
                if sub_obj.get("id") == _id:
                    return obj.get("id")


class VNFDAgent(SubAgent):
    def __init__(self, client, project_id, main_agent):
        super(VNFDAgent, self).__init__(client=client,
                                        project_id=project_id,
                                        main_agent=main_agent,
                                        sub_url='vnfdescriptors',
                                        sub_obj="vnfd")


class VNFRAgent(SubAgent):
    def __init__(self, client, project_id, main_agent):
        super(VNFRAgent, self).__init__(client=client,
                                        project_id=project_id,
                                        main_agent=main_agent,
                                        sub_url='vnfrecords',
                                        sub_obj="vnfr")


class OpenBatonAgentFactory(object):
    def __init__(self, nfvo_ip="localhost", nfvo_port="8080", https=False, version=1, username=None, password=None,
                 project_id=None):

        self.nfvo_ip = nfvo_ip
        self.nfvo_port = nfvo_port
        self.https = https
        self.version = version
        self.username = username

        self.password = password
        self._client = RestClient(nfvo_ip=self.nfvo_ip,
                                  nfvo_port=self.nfvo_port,
                                  https=self.https,
                                  version=self.version,
                                  username=self.username,
                                  password=self.password,
                                  project_id=project_id)

        self._project_agent = None
        self._event_agent = None
        self._vim_instance_agent = None
        self._ns_records_agent = None
        self._ns_descriptor_agent = None
        self._vnf_package_agent = None
        self._vnf_descriptor_agent = None
        self._vnf_record_agent = None
        self._market_agent = None
        self._user_agent = None
        self._csarnsd_agent = None
        self._csarvnfd_agent = None
        self._key_agent = None
        self._log_agent = None

    def get_project_agent(self):
        if self._project_agent is None:
            self._project_agent = ProjectAgent(self._client)
        return self._project_agent

    def get_event_agent(self, project_id):
        if self._event_agent is None:
            self._event_agent = EventAgent(self._client, project_id=project_id)
        self._event_agent.project_id = project_id
        return self._event_agent

    def get_vim_instance_agent(self, project_id):
        if self._vim_instance_agent is None:
            self._vim_instance_agent = VimInstanceAgent(self._client, project_id=project_id)
        self._vim_instance_agent.project_id = project_id
        return self._vim_instance_agent

    def get_ns_records_agent(self, project_id):
        if self._ns_records_agent is None:
            self._ns_records_agent = NSRAgent(self._client, project_id=project_id)
        self._ns_records_agent.project_id = project_id
        return self._ns_records_agent

    def get_ns_descriptor_agent(self, project_id):
        if self._ns_descriptor_agent is None:
            self._ns_descriptor_agent = NSDAgent(self._client, project_id=project_id)
        self._ns_descriptor_agent.project_id = project_id
        return self._ns_descriptor_agent

    def get_vnf_descriptor_agent(self, project_id):
        self.get_ns_descriptor_agent(project_id=project_id)
        if self._vnf_descriptor_agent is None:
            self._vnf_descriptor_agent = VNFDAgent(client=self._client,
                                                   project_id=project_id,
                                                   main_agent=self._ns_descriptor_agent)
        self._vnf_descriptor_agent.project_id = project_id
        return self._vnf_descriptor_agent

    def get_market_agent(self, project_id):
        if self._market_agent is None:
            self._market_agent = MarketAgent(self._client, project_id=project_id)
        self._market_agent.project_id = project_id
        return self._market_agent

    def get_user_agent(self, project_id):
        if self._user_agent is None:
            self._user_agent = UserAgent(self._client, project_id=project_id)
        self._user_agent.project_id = project_id
        return self._user_agent

    def get_csarnsd_agent(self, project_id):
        if self._csarnsd_agent is None:
            self._csarnsd_agent = CSARNSDAgent(self._client, project_id=project_id)
        self._csarnsd_agent.project_id = project_id
        return self._csarnsd_agent

    def get_csarvnfd_agent(self, project_id):
        if self._csarvnfd_agent is None:
            self._csarvnfd_agent = CSARVNFDAgent(self._client, project_id=project_id)
        self._csarvnfd_agent.project_id = project_id
        return self._csarvnfd_agent

    def get_vnf_record_agent(self, project_id):
        self.get_ns_records_agent(project_id=project_id)
        if self._vnf_record_agent is None:
            self._vnf_record_agent = VNFRAgent(self._client, project_id=project_id, main_agent=self._ns_records_agent)
        self._vnf_record_agent.project_id = project_id
        return self._vnf_record_agent

    def get_vnf_package_agent(self, project_id):
        if self._vnf_package_agent is None:
            self._vnf_package_agent = VNFPackageAgent(self._client, project_id=project_id)
        self._vnf_package_agent.project_id = project_id
        return self._vnf_package_agent

    def get_key_agent(self, project_id):
        if self._key_agent is None:
            self._key_agent = KeyAgent(self._client, project_id=project_id)
        self._key_agent.project_id = project_id
        return self._key_agent

    def get_log_agent(self, project_id):
        if self._log_agent is None:
            self._log_agent = LogAgent(self._client, project_id=project_id)
        self._log_agent.project_id = project_id
        return self._log_agent

    def get_agent(self, agent, project_id):
        if agent == "nsr":
            return self.get_ns_records_agent(project_id)
        if agent == "nsd":
            return self.get_ns_descriptor_agent(project_id)
        if agent == "vnfd":
            return self.get_vnf_descriptor_agent(project_id)
        if agent == "vnfr":
            return self.get_vnf_record_agent(project_id)
        if agent == "vim":
            return self.get_vim_instance_agent(project_id)
        if agent == "vnfpackage":
            return self.get_vnf_package_agent(project_id)
        if agent == "project":
            return self.get_project_agent()
        if agent == "event":
            return self.get_event_agent(project_id)
        if agent == "market":
            return self.get_market_agent(project_id)
        if agent == "user":
            return self.get_user_agent(project_id)
        if agent == "csarnsd":
            return self.get_csarnsd_agent(project_id)
        if agent == "csarvnfd":
            return self.get_csarvnfd_agent(project_id)
        if agent == "key":
            return self.get_key_agent(project_id)
        if agent == "log":
            return self.get_log_agent(project_id)

        raise WrongParameters('Agent %s not found' % agent)
