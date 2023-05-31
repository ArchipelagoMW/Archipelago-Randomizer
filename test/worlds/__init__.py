def load_tests(loader, standard_tests, pattern):
    import os
    import unittest
    from ..TestBase import file_path
    from worlds.AutoWorld import AutoWorldRegister

    suite = unittest.TestSuite()
    suite.addTests(standard_tests)
    folders = [os.path.join(os.path.split(world.__file__)[0], "test")
               for world in AutoWorldRegister.world_types.values()]
    all_tests = []
    for folder in folders:
        if os.path.exists(folder):
            for test_collection in loader.discover(folder, top_level_dir=file_path):
                for test_suite in test_collection:
                    for test_case in test_suite:
                        all_tests.append(test_case)

    suite.addTests(sorted(all_tests, key=lambda test: test.__module__))
    return suite
