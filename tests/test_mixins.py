from rest_framework import mixins

import rest_framework_mixins


def test_all_bases_have_their_initials():
    for module_attribute_name in dir(rest_framework_mixins):
        if not module_attribute_name.endswith("Mixin"):
            continue

        initials = module_attribute_name.replace("Mixin", "")
        mixin = getattr(rest_framework_mixins, module_attribute_name)
        bases = mixin.__bases__

        for base in bases:
            if base in (
                rest_framework_mixins.NoPutMixin,
                rest_framework_mixins.NoPatchMixin,
            ):
                continue

            initial = base.__name__[0]
            if initial == "U" and rest_framework_mixins.NoPutMixin in bases:
                initial = "P"

            assert initial in initials


def test_all_initials_have_bases():
    for module_attribute_name in dir(rest_framework_mixins):
        if not module_attribute_name.endswith("Mixin"):
            continue
        if module_attribute_name in ("NoPatchMixin", "NoPutMixin"):
            continue

        initials = module_attribute_name.replace("Mixin", "")
        mixin = getattr(rest_framework_mixins, module_attribute_name)
        bases = mixin.__bases__

        initial_map = {
            "L": mixins.ListModelMixin,
            "R": mixins.RetrieveModelMixin,
            "C": mixins.CreateModelMixin,
            "U": mixins.UpdateModelMixin,
            "P": mixins.UpdateModelMixin,
            "D": mixins.DestroyModelMixin,
        }

        for initial in initials:
            assert initial_map[initial] in bases
