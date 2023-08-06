"""AuthZ Adapter implementations of assessment.authoring managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification


from . import sessions
from ..osid import managers as osid_managers
from ..osid.osid_errors import Unimplemented
from ..osid.osid_errors import Unimplemented, OperationFailed, Unsupported
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from ..utilities import raise_null_argument
from dlkit.manager_impls.assessment_authoring import managers as assessment_authoring_managers


class AssessmentAuthoringProfile(osid_managers.OsidProfile, assessment_authoring_managers.AssessmentAuthoringProfile):
    """Adapts underlying AssessmentAuthoringProfile methodswith authorization checks."""
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        base_package_mgr = self._get_base_package_provider_manager('assessment', proxy)
        if proxy is not None:
            try:
                return base_package_mgr.get_bank_hierarchy_session(proxy)
            except Unsupported:
                return None
        try:
            return base_package_mgr.get_bank_hierarchy_session()
        except Unsupported:
            return None

    def _get_base_package_provider_manager(self, base_package, proxy=None):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(base_package))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        # try:
        #     # need to add version argument
        #     return self._my_runtime.get_proxy_manager(base_package.upper(), provider_impl)
        # except AttributeError:
        #     # need to add version argument
        #     return self._my_runtime.get_manager(base_package.upper(), provider_impl)
        if proxy is not None:
            # need to add version argument
            return self._my_runtime.get_proxy_manager(base_package.upper(), provider_impl)
        else:
            # need to add version argument
            return self._my_runtime.get_manager(base_package.upper(), provider_impl)

    def supports_assessment_part_lookup(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_assessment_part_lookup
        return self._provider_manager.supports_assessment_part_lookup()

    def supports_assessment_part_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_part_query()

    def supports_assessment_part_admin(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_assessment_part_admin
        return self._provider_manager.supports_assessment_part_admin()

    def supports_assessment_part_item(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_assessment_part_item
        return self._provider_manager.supports_assessment_part_item()

    def supports_assessment_part_item_design(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_assessment_part_item_design
        return self._provider_manager.supports_assessment_part_item_design()

    def supports_sequence_rule_lookup(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_sequence_rule_lookup
        return self._provider_manager.supports_sequence_rule_lookup()

    def supports_sequence_rule_admin(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.supports_sequence_rule_admin
        return self._provider_manager.supports_sequence_rule_admin()

    def get_assessment_part_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_assessment_part_record_types
        return self._provider_manager.get_assessment_part_record_types()

    assessment_part_record_types = property(fget=get_assessment_part_record_types)

    assessment_part_record_types = property(fget=get_assessment_part_record_types)

    def get_assessment_part_search_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_assessment_part_search_record_types
        return self._provider_manager.get_assessment_part_search_record_types()

    assessment_part_search_record_types = property(fget=get_assessment_part_search_record_types)

    assessment_part_search_record_types = property(fget=get_assessment_part_search_record_types)

    def get_sequence_rule_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_sequence_rule_record_types
        return self._provider_manager.get_sequence_rule_record_types()

    sequence_rule_record_types = property(fget=get_sequence_rule_record_types)

    sequence_rule_record_types = property(fget=get_sequence_rule_record_types)

    def get_sequence_rule_search_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_sequence_rule_search_record_types
        return self._provider_manager.get_sequence_rule_search_record_types()

    sequence_rule_search_record_types = property(fget=get_sequence_rule_search_record_types)

    sequence_rule_search_record_types = property(fget=get_sequence_rule_search_record_types)

    def get_sequence_rule_enabler_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_sequence_rule_enabler_record_types
        return self._provider_manager.get_sequence_rule_enabler_record_types()

    sequence_rule_enabler_record_types = property(fget=get_sequence_rule_enabler_record_types)

    sequence_rule_enabler_record_types = property(fget=get_sequence_rule_enabler_record_types)

    def get_sequence_rule_enabler_search_record_types(self):
        # Implemented from azosid template for -
        # osid.assessment_authoring.AssessmentAuthoringProfile.get_sequence_rule_enabler_search_record_types
        return self._provider_manager.get_sequence_rule_enabler_search_record_types()

    sequence_rule_enabler_search_record_types = property(fget=get_sequence_rule_enabler_search_record_types)

    sequence_rule_enabler_search_record_types = property(fget=get_sequence_rule_enabler_search_record_types)


class AssessmentAuthoringManager(osid_managers.OsidManager, AssessmentAuthoringProfile, assessment_authoring_managers.AssessmentAuthoringManager):
    """Adapts underlying AssessmentAuthoringManager methodswith authorization checks."""
    def __init__(self):
        AssessmentAuthoringProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:assessment_authoringProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('ASSESSMENT_AUTHORING', provider_impl)
        # need to add version argument

    def get_assessment_part_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session()
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartLookupSession')(
                provider_session=self._provider_manager.get_assessment_part_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_part_lookup_session = property(fget=get_assessment_part_lookup_session)

    @raise_null_argument
    def get_assessment_part_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartLookupSession')(
                provider_session=self._provider_manager.get_assessment_part_lookup_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session()
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartQuerySession')(
                provider_session=self._provider_manager.get_assessment_part_query_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_part_query_session = property(fget=get_assessment_part_query_session)

    @raise_null_argument
    def get_assessment_part_query_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartQuerySession')(
                provider_session=self._provider_manager.get_assessment_part_query_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentPartAdminSession')(
                provider_session=self._provider_manager.get_assessment_part_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    assessment_part_admin_session = property(fget=get_assessment_part_admin_session)

    @raise_null_argument
    def get_assessment_part_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentPartAdminSession')(
                provider_session=self._provider_manager.get_assessment_part_admin_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_sequence_rule_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_sequence_rule_query_session()
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'SequenceRuleLookupSession')(
                provider_session=self._provider_manager.get_sequence_rule_lookup_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    sequence_rule_lookup_session = property(fget=get_sequence_rule_lookup_session)

    @raise_null_argument
    def get_sequence_rule_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_sequence_rule_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'SequenceRuleLookupSession')(
                provider_session=self._provider_manager.get_sequence_rule_lookup_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_sequence_rule_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'SequenceRuleAdminSession')(
                provider_session=self._provider_manager.get_sequence_rule_admin_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    sequence_rule_admin_session = property(fget=get_sequence_rule_admin_session)

    @raise_null_argument
    def get_sequence_rule_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'SequenceRuleAdminSession')(
                provider_session=self._provider_manager.get_sequence_rule_admin_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_item_session(self):
        try:
            return getattr(sessions, 'AssessmentPartItemSession')(
                provider_session=self._provider_manager.get_assessment_part_item_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    def get_assessment_part_item_session_for_bank(self, bank_id):
        try:
            return getattr(sessions, 'AssessmentPartItemSession')(
                provider_session=self._provider_manager.get_assessment_part_item_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_item_design_session(self):
        try:
            return getattr(sessions, 'AssessmentPartItemDesignSession')(
                provider_session=self._provider_manager.get_assessment_part_item_design_session(),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    def get_assessment_part_item_design_session_for_bank(self, bank_id):
        try:
            return getattr(sessions, 'AssessmentPartItemDesignSession')(
                provider_session=self._provider_manager.get_assessment_part_item_design_session_for_bank(bank_id),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager)
        except AttributeError:
            raise OperationFailed()


class AssessmentAuthoringProxyManager(osid_managers.OsidProxyManager, AssessmentAuthoringProfile, assessment_authoring_managers.AssessmentAuthoringProxyManager):
    """Adapts underlying AssessmentAuthoringProxyManager methodswith authorization checks."""
    def __init__(self):
        AssessmentAuthoringProfile.__init__(self)

    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:assessment_authoringProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('ASSESSMENT_AUTHORING', provider_impl)
        # need to add version argument

    @raise_null_argument
    def get_assessment_part_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartLookupSession')(
                provider_session=self._provider_manager.get_assessment_part_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_assessment_part_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartLookupSession')(
                provider_session=self._provider_manager.get_assessment_part_lookup_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_assessment_part_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartQuerySession')(
                provider_session=self._provider_manager.get_assessment_part_query_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_assessment_part_query_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_part_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentPartQuerySession')(
                provider_session=self._provider_manager.get_assessment_part_query_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_assessment_part_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentPartAdminSession')(
                provider_session=self._provider_manager.get_assessment_part_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_assessment_part_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentPartAdminSession')(
                provider_session=self._provider_manager.get_assessment_part_admin_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_sequence_rule_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_sequence_rule_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'SequenceRuleLookupSession')(
                provider_session=self._provider_manager.get_sequence_rule_lookup_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_sequence_rule_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_sequence_rule_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unimplemented:
            query_session = None
        try:
            return getattr(sessions, 'SequenceRuleLookupSession')(
                provider_session=self._provider_manager.get_sequence_rule_lookup_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                proxy=proxy,
                hierarchy_session=self._get_hierarchy_session(proxy),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_sequence_rule_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'SequenceRuleAdminSession')(
                provider_session=self._provider_manager.get_sequence_rule_admin_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    @raise_null_argument
    def get_sequence_rule_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'SequenceRuleAdminSession')(
                provider_session=self._provider_manager.get_sequence_rule_admin_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_item_session(self, proxy):
        try:
            return getattr(sessions, 'AssessmentPartItemSession')(
                provider_session=self._provider_manager.get_assessment_part_item_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    def get_assessment_part_item_session_for_bank(self, bank_id, proxy):
        try:
            return getattr(sessions, 'AssessmentPartItemSession')(
                provider_session=self._provider_manager.get_assessment_part_item_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_part_item_design_session(self, proxy):
        try:
            return getattr(sessions, 'AssessmentPartItemDesignSession')(
                provider_session=self._provider_manager.get_assessment_part_item_design_session(proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    def get_assessment_part_item_design_session_for_bank(self, bank_id, proxy):
        try:
            return getattr(sessions, 'AssessmentPartItemDesignSession')(
                provider_session=self._provider_manager.get_assessment_part_item_design_session_for_bank(bank_id, proxy),
                authz_session=self._get_authz_session(),
                override_lookup_session=self._get_override_lookup_session(),
                provider_manager=self._provider_manager,
                proxy=proxy)
        except AttributeError:
            raise OperationFailed()
