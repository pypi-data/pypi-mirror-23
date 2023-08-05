# [Changelog](https://github.com/halkeye/flask_atlassian_connect/releases)

## [0.0.1](https://github.com/halkeye/flask_atlassian_connect/compare/0.0.0...0.0.1)

* [b850fe3](https://github.com/halkeye/flask_atlassian_connect/commit/b850fe3) fix up docs
* [1dc0cf2](https://github.com/halkeye/flask_atlassian_connect/commit/1dc0cf2) delete/all/save/load of Client
* [f04425a](https://github.com/halkeye/flask_atlassian_connect/commit/f04425a) feat: add tasks() function that will return a pyinvoke collection
* [d38974d](https://github.com/halkeye/flask_atlassian_connect/commit/d38974d) fix: App is not necessarily defined at creation, move full link creation to when desciptor is being outputted
* [7d327eb](https://github.com/halkeye/flask_atlassian_connect/commit/7d327eb) slight docs cleanup
* [5e8dbcc](https://github.com/halkeye/flask_atlassian_connect/commit/5e8dbcc) Feat: add atlassian_jwt_post_url template variable to code/docs
* [05aa955](https://github.com/halkeye/flask_atlassian_connect/commit/05aa955) Rename Client to AtlassianConnectClient
* [36dffe8](https://github.com/halkeye/flask_atlassian_connect/commit/36dffe8) fix flake8 warning
* [df0c584](https://github.com/halkeye/flask_atlassian_connect/commit/df0c584) fix: Handle functions returning strings or templates, and only default if nothing is provided
* [c6d8248](https://github.com/halkeye/flask_atlassian_connect/commit/c6d8248) Add some simple configuration. Clean it up later
* [5d050d7](https://github.com/halkeye/flask_atlassian_connect/commit/5d050d7) move the .nojekyll support to sphix so its a little cleaner
* [ca6c30a](https://github.com/halkeye/flask_atlassian_connect/commit/ca6c30a) add .nojekyll
* [c05c8ff](https://github.com/halkeye/flask_atlassian_connect/commit/c05c8ff) Ahhh, GH_TOKEN should be an env variable, and referenced in the deploy
* [4876e00](https://github.com/halkeye/flask_atlassian_connect/commit/4876e00) deploy docs to gh-pages
* [2991fd6](https://github.com/halkeye/flask_atlassian_connect/commit/2991fd6) meh commit to re trigger travis
* [b98b9e9](https://github.com/halkeye/flask_atlassian_connect/commit/b98b9e9) install sphix stuff after everything else is tested so it can't mess with things
* [9daa450](https://github.com/halkeye/flask_atlassian_connect/commit/9daa450) webpanel documentation
* [ad59663](https://github.com/halkeye/flask_atlassian_connect/commit/ad59663) docs: flesh out the lifecycle docs a bit more
* [4143191](https://github.com/halkeye/flask_atlassian_connect/commit/4143191) docs: Adding webhook and module decorator docs
* [5d524f2](https://github.com/halkeye/flask_atlassian_connect/commit/5d524f2) don't double test on travis
* [3ca4b9b](https://github.com/halkeye/flask_atlassian_connect/commit/3ca4b9b) docs: fix a little bit of earlier copy and pate
* [c77e3c2](https://github.com/halkeye/flask_atlassian_connect/commit/c77e3c2) add some more webhooks documentation
* [5fa170e](https://github.com/halkeye/flask_atlassian_connect/commit/5fa170e) docs: remove rogue import from docs
* [7823ce2](https://github.com/halkeye/flask_atlassian_connect/commit/7823ce2) lets try deploying docs after a build
* [e3142fb](https://github.com/halkeye/flask_atlassian_connect/commit/e3142fb) Logo support for documentation
* [9a28e68](https://github.com/halkeye/flask_atlassian_connect/commit/9a28e68) I like these docs now
* [14137cc](https://github.com/halkeye/flask_atlassian_connect/commit/14137cc) 3.6 is hard, later later later
* [3c75cff](https://github.com/halkeye/flask_atlassian_connect/commit/3c75cff) remove print statement so python 3 can run again. and its not needed
* [957ce1b](https://github.com/halkeye/flask_atlassian_connect/commit/957ce1b) test in python 3 too
* [5784c55](https://github.com/halkeye/flask_atlassian_connect/commit/5784c55) remove old pandoc stuff
* [3a78968](https://github.com/halkeye/flask_atlassian_connect/commit/3a78968) Fix that encryption, was pointed at the wrong travis repo
* [284565e](https://github.com/halkeye/flask_atlassian_connect/commit/284565e) remove some extra whitespace
* [ff7371a](https://github.com/halkeye/flask_atlassian_connect/commit/ff7371a) make setup.py great again
* [422ec08](https://github.com/halkeye/flask_atlassian_connect/commit/422ec08) fix a couple warnings
* [f23732e](https://github.com/halkeye/flask_atlassian_connect/commit/f23732e) Starting documentation
* [39dc6b8](https://github.com/halkeye/flask_atlassian_connect/commit/39dc6b8) Clean up reference client class so its a bit more useful
* [b94eaaa](https://github.com/halkeye/flask_atlassian_connect/commit/b94eaaa) cleanup
* [36b8b79](https://github.com/halkeye/flask_atlassian_connect/commit/36b8b79) rewrite based on what i've learned over the last couple of weeks. Should mostly comply to pypi standards now
* [f5f8964](https://github.com/halkeye/flask_atlassian_connect/commit/f5f8964) fix: make sure to return the actual webhook function so it can still be manually called
* [7c1b8dd](https://github.com/halkeye/flask_atlassian_connect/commit/7c1b8dd) feat: handle events routing for you. decorator will just do event handling
* [69f9f92](https://github.com/halkeye/flask_atlassian_connect/commit/69f9f92) skip cleanup on travis for deploys
* [b7cb11b](https://github.com/halkeye/flask_atlassian_connect/commit/b7cb11b) 0.0.2
* [21e8c77](https://github.com/halkeye/flask_atlassian_connect/commit/21e8c77) refactor: attempt to reduce the amount of duplicated code in tests
* [5e909c6](https://github.com/halkeye/flask_atlassian_connect/commit/5e909c6) feat: basic module decorator test
* [f2e6d69](https://github.com/halkeye/flask_atlassian_connect/commit/f2e6d69) feat: Tests for webpanel
* [811dd57](https://github.com/halkeye/flask_atlassian_connect/commit/811dd57) refactor: Replace the descriptor with direct functions to make pylint stop whining
* [4866785](https://github.com/halkeye/flask_atlassian_connect/commit/4866785) Figured out why i suddenly had a lot of debug messages, remove global debugging logic
* [59e44d0](https://github.com/halkeye/flask_atlassian_connect/commit/59e44d0) more codacy
* [46e07a4](https://github.com/halkeye/flask_atlassian_connect/commit/46e07a4) ci: codacy code coverage util
* [ad82aa4](https://github.com/halkeye/flask_atlassian_connect/commit/ad82aa4) refactor: Fix up minor issues reported by codacy
* [904cbbc](https://github.com/halkeye/flask_atlassian_connect/commit/904cbbc) remove trailing space
* [0847697](https://github.com/halkeye/flask_atlassian_connect/commit/0847697) fix: python setup.py tests will now run the right directory
* [df27ae2](https://github.com/halkeye/flask_atlassian_connect/commit/df27ae2) fix: tell setuptools to autofind packages after i forgot to fix it after the last refactor
* [8a13423](https://github.com/halkeye/flask_atlassian_connect/commit/8a13423) feat: basic webhook support
* [c32eb7e](https://github.com/halkeye/flask_atlassian_connect/commit/c32eb7e) feat: support overring list of scopes
* [e1f9614](https://github.com/halkeye/flask_atlassian_connect/commit/e1f9614) ci: RAWR. try having no specific requirements for version
* [2ff1886](https://github.com/halkeye/flask_atlassian_connect/commit/2ff1886) ci: RAWR. try having no specific requirements for version
* [e276722](https://github.com/halkeye/flask_atlassian_connect/commit/e276722) ci: RAWR. try having no specific requirements for version
* [619bc33](https://github.com/halkeye/flask_atlassian_connect/commit/619bc33) fix: version conflict for mock
* [463b53a](https://github.com/halkeye/flask_atlassian_connect/commit/463b53a) ci: donno why this is working locally and not in travis
* [54fc104](https://github.com/halkeye/flask_atlassian_connect/commit/54fc104) ci: upgrade pip, remove pandoc
* [265ee6f](https://github.com/halkeye/flask_atlassian_connect/commit/265ee6f) ci: donno why this is working locally and not in travis
* [d6cc7f8](https://github.com/halkeye/flask_atlassian_connect/commit/d6cc7f8) fix: make sure all testing requirements are installed when running tests
* [693aaf2](https://github.com/halkeye/flask_atlassian_connect/commit/693aaf2) ci: Tell travis to run tests
* [9ade918](https://github.com/halkeye/flask_atlassian_connect/commit/9ade918) fix: dependancies should be set to minimum version
* [55c7d39](https://github.com/halkeye/flask_atlassian_connect/commit/55c7d39) fix: require the new 1.8.1 version of atlassian_jwt
* [e004f63](https://github.com/halkeye/flask_atlassian_connect/commit/e004f63) cleanup based on other modules i've found online
* [9b90c26](https://github.com/halkeye/flask_atlassian_connect/commit/9b90c26) refactor: don't need mock and reqeusts and stuff except for running tests
* [c421779](https://github.com/halkeye/flask_atlassian_connect/commit/c421779) fix: fix name matching
* [e7f851f](https://github.com/halkeye/flask_atlassian_connect/commit/e7f851f) fix: Most of the type client is going to be an object not a dict
* [a779f27](https://github.com/halkeye/flask_atlassian_connect/commit/a779f27) cleanup based on other modules i've found online
* [1ff66d5](https://github.com/halkeye/flask_atlassian_connect/commit/1ff66d5) don't need mock and reqeusts and stuff except for running tests
* [a247c7c](https://github.com/halkeye/flask_atlassian_connect/commit/a247c7c) fix name matching
* [4458a2e](https://github.com/halkeye/flask_atlassian_connect/commit/4458a2e) Most of the type client is going to be an object not a dict
* [961a138](https://github.com/halkeye/flask_atlassian_connect/commit/961a138) shrug at this point
* [306834f](https://github.com/halkeye/flask_atlassian_connect/commit/306834f) Travis
* [5657e56](https://github.com/halkeye/flask_atlassian_connect/commit/5657e56) fix install
* [b318a8a](https://github.com/halkeye/flask_atlassian_connect/commit/b318a8a) fun times travis testing
* [57c30ee](https://github.com/halkeye/flask_atlassian_connect/commit/57c30ee) make sure readme is installed with the package
* [5cd7aa5](https://github.com/halkeye/flask_atlassian_connect/commit/5cd7aa5) use default container based images
* [789f9ea](https://github.com/halkeye/flask_atlassian_connect/commit/789f9ea) pandoc
* [b66dbcd](https://github.com/halkeye/flask_atlassian_connect/commit/b66dbcd) build build build
* [04218f4](https://github.com/halkeye/flask_atlassian_connect/commit/04218f4) "python setup.py test" works now
* [4999de7](https://github.com/halkeye/flask_atlassian_connect/commit/4999de7) init

## [0.0.3](https://github.com/halkeye/flask_atlassian_connect/compare/0.0.2...0.0.3)

* [b850fe3](https://github.com/halkeye/flask_atlassian_connect/commit/b850fe3) fix up docs
* [1dc0cf2](https://github.com/halkeye/flask_atlassian_connect/commit/1dc0cf2) delete/all/save/load of Client
* [f04425a](https://github.com/halkeye/flask_atlassian_connect/commit/f04425a) feat: add tasks() function that will return a pyinvoke collection
* [d38974d](https://github.com/halkeye/flask_atlassian_connect/commit/d38974d) fix: App is not necessarily defined at creation, move full link creation to when desciptor is being outputted
* [7d327eb](https://github.com/halkeye/flask_atlassian_connect/commit/7d327eb) slight docs cleanup
* [5e8dbcc](https://github.com/halkeye/flask_atlassian_connect/commit/5e8dbcc) Feat: add atlassian_jwt_post_url template variable to code/docs
* [05aa955](https://github.com/halkeye/flask_atlassian_connect/commit/05aa955) Rename Client to AtlassianConnectClient
* [36dffe8](https://github.com/halkeye/flask_atlassian_connect/commit/36dffe8) fix flake8 warning
* [df0c584](https://github.com/halkeye/flask_atlassian_connect/commit/df0c584) fix: Handle functions returning strings or templates, and only default if nothing is provided
* [c6d8248](https://github.com/halkeye/flask_atlassian_connect/commit/c6d8248) Add some simple configuration. Clean it up later
* [5d050d7](https://github.com/halkeye/flask_atlassian_connect/commit/5d050d7) move the .nojekyll support to sphix so its a little cleaner
* [ca6c30a](https://github.com/halkeye/flask_atlassian_connect/commit/ca6c30a) add .nojekyll
* [c05c8ff](https://github.com/halkeye/flask_atlassian_connect/commit/c05c8ff) Ahhh, GH_TOKEN should be an env variable, and referenced in the deploy
* [4876e00](https://github.com/halkeye/flask_atlassian_connect/commit/4876e00) deploy docs to gh-pages
* [2991fd6](https://github.com/halkeye/flask_atlassian_connect/commit/2991fd6) meh commit to re trigger travis
* [b98b9e9](https://github.com/halkeye/flask_atlassian_connect/commit/b98b9e9) install sphix stuff after everything else is tested so it can't mess with things
* [9daa450](https://github.com/halkeye/flask_atlassian_connect/commit/9daa450) webpanel documentation
* [ad59663](https://github.com/halkeye/flask_atlassian_connect/commit/ad59663) docs: flesh out the lifecycle docs a bit more
* [4143191](https://github.com/halkeye/flask_atlassian_connect/commit/4143191) docs: Adding webhook and module decorator docs
* [5d524f2](https://github.com/halkeye/flask_atlassian_connect/commit/5d524f2) don't double test on travis
* [3ca4b9b](https://github.com/halkeye/flask_atlassian_connect/commit/3ca4b9b) docs: fix a little bit of earlier copy and pate
* [c77e3c2](https://github.com/halkeye/flask_atlassian_connect/commit/c77e3c2) add some more webhooks documentation
* [5fa170e](https://github.com/halkeye/flask_atlassian_connect/commit/5fa170e) docs: remove rogue import from docs
* [7823ce2](https://github.com/halkeye/flask_atlassian_connect/commit/7823ce2) lets try deploying docs after a build
* [e3142fb](https://github.com/halkeye/flask_atlassian_connect/commit/e3142fb) Logo support for documentation
* [9a28e68](https://github.com/halkeye/flask_atlassian_connect/commit/9a28e68) I like these docs now
* [14137cc](https://github.com/halkeye/flask_atlassian_connect/commit/14137cc) 3.6 is hard, later later later
* [3c75cff](https://github.com/halkeye/flask_atlassian_connect/commit/3c75cff) remove print statement so python 3 can run again. and its not needed
* [957ce1b](https://github.com/halkeye/flask_atlassian_connect/commit/957ce1b) test in python 3 too
* [5784c55](https://github.com/halkeye/flask_atlassian_connect/commit/5784c55) remove old pandoc stuff
* [3a78968](https://github.com/halkeye/flask_atlassian_connect/commit/3a78968) Fix that encryption, was pointed at the wrong travis repo
* [284565e](https://github.com/halkeye/flask_atlassian_connect/commit/284565e) remove some extra whitespace
* [ff7371a](https://github.com/halkeye/flask_atlassian_connect/commit/ff7371a) make setup.py great again
* [422ec08](https://github.com/halkeye/flask_atlassian_connect/commit/422ec08) fix a couple warnings
* [f23732e](https://github.com/halkeye/flask_atlassian_connect/commit/f23732e) Starting documentation
* [39dc6b8](https://github.com/halkeye/flask_atlassian_connect/commit/39dc6b8) Clean up reference client class so its a bit more useful
* [b94eaaa](https://github.com/halkeye/flask_atlassian_connect/commit/b94eaaa) cleanup
* [36b8b79](https://github.com/halkeye/flask_atlassian_connect/commit/36b8b79) rewrite based on what i've learned over the last couple of weeks. Should mostly comply to pypi standards now
* [f5f8964](https://github.com/halkeye/flask_atlassian_connect/commit/f5f8964) fix: make sure to return the actual webhook function so it can still be manually called
* [7c1b8dd](https://github.com/halkeye/flask_atlassian_connect/commit/7c1b8dd) feat: handle events routing for you. decorator will just do event handling
* [69f9f92](https://github.com/halkeye/flask_atlassian_connect/commit/69f9f92) skip cleanup on travis for deploys
* [b7cb11b](https://github.com/halkeye/flask_atlassian_connect/commit/b7cb11b) 0.0.2
* [21e8c77](https://github.com/halkeye/flask_atlassian_connect/commit/21e8c77) refactor: attempt to reduce the amount of duplicated code in tests
* [5e909c6](https://github.com/halkeye/flask_atlassian_connect/commit/5e909c6) feat: basic module decorator test
* [f2e6d69](https://github.com/halkeye/flask_atlassian_connect/commit/f2e6d69) feat: Tests for webpanel
* [811dd57](https://github.com/halkeye/flask_atlassian_connect/commit/811dd57) refactor: Replace the descriptor with direct functions to make pylint stop whining
* [4866785](https://github.com/halkeye/flask_atlassian_connect/commit/4866785) Figured out why i suddenly had a lot of debug messages, remove global debugging logic
* [59e44d0](https://github.com/halkeye/flask_atlassian_connect/commit/59e44d0) more codacy
* [46e07a4](https://github.com/halkeye/flask_atlassian_connect/commit/46e07a4) ci: codacy code coverage util
* [ad82aa4](https://github.com/halkeye/flask_atlassian_connect/commit/ad82aa4) refactor: Fix up minor issues reported by codacy
* [904cbbc](https://github.com/halkeye/flask_atlassian_connect/commit/904cbbc) remove trailing space
* [0847697](https://github.com/halkeye/flask_atlassian_connect/commit/0847697) fix: python setup.py tests will now run the right directory
* [df27ae2](https://github.com/halkeye/flask_atlassian_connect/commit/df27ae2) fix: tell setuptools to autofind packages after i forgot to fix it after the last refactor
* [8a13423](https://github.com/halkeye/flask_atlassian_connect/commit/8a13423) feat: basic webhook support
* [c32eb7e](https://github.com/halkeye/flask_atlassian_connect/commit/c32eb7e) feat: support overring list of scopes
* [e1f9614](https://github.com/halkeye/flask_atlassian_connect/commit/e1f9614) ci: RAWR. try having no specific requirements for version
* [2ff1886](https://github.com/halkeye/flask_atlassian_connect/commit/2ff1886) ci: RAWR. try having no specific requirements for version
* [e276722](https://github.com/halkeye/flask_atlassian_connect/commit/e276722) ci: RAWR. try having no specific requirements for version
* [619bc33](https://github.com/halkeye/flask_atlassian_connect/commit/619bc33) fix: version conflict for mock
* [463b53a](https://github.com/halkeye/flask_atlassian_connect/commit/463b53a) ci: donno why this is working locally and not in travis
* [54fc104](https://github.com/halkeye/flask_atlassian_connect/commit/54fc104) ci: upgrade pip, remove pandoc
* [265ee6f](https://github.com/halkeye/flask_atlassian_connect/commit/265ee6f) ci: donno why this is working locally and not in travis
* [d6cc7f8](https://github.com/halkeye/flask_atlassian_connect/commit/d6cc7f8) fix: make sure all testing requirements are installed when running tests
* [693aaf2](https://github.com/halkeye/flask_atlassian_connect/commit/693aaf2) ci: Tell travis to run tests
* [9ade918](https://github.com/halkeye/flask_atlassian_connect/commit/9ade918) fix: dependancies should be set to minimum version
* [55c7d39](https://github.com/halkeye/flask_atlassian_connect/commit/55c7d39) fix: require the new 1.8.1 version of atlassian_jwt
* [e004f63](https://github.com/halkeye/flask_atlassian_connect/commit/e004f63) cleanup based on other modules i've found online
* [9b90c26](https://github.com/halkeye/flask_atlassian_connect/commit/9b90c26) refactor: don't need mock and reqeusts and stuff except for running tests
* [c421779](https://github.com/halkeye/flask_atlassian_connect/commit/c421779) fix: fix name matching
* [e7f851f](https://github.com/halkeye/flask_atlassian_connect/commit/e7f851f) fix: Most of the type client is going to be an object not a dict
* [a779f27](https://github.com/halkeye/flask_atlassian_connect/commit/a779f27) cleanup based on other modules i've found online
* [1ff66d5](https://github.com/halkeye/flask_atlassian_connect/commit/1ff66d5) don't need mock and reqeusts and stuff except for running tests
* [a247c7c](https://github.com/halkeye/flask_atlassian_connect/commit/a247c7c) fix name matching
* [4458a2e](https://github.com/halkeye/flask_atlassian_connect/commit/4458a2e) Most of the type client is going to be an object not a dict
* [961a138](https://github.com/halkeye/flask_atlassian_connect/commit/961a138) shrug at this point
* [306834f](https://github.com/halkeye/flask_atlassian_connect/commit/306834f) Travis
* [5657e56](https://github.com/halkeye/flask_atlassian_connect/commit/5657e56) fix install
* [b318a8a](https://github.com/halkeye/flask_atlassian_connect/commit/b318a8a) fun times travis testing
* [57c30ee](https://github.com/halkeye/flask_atlassian_connect/commit/57c30ee) make sure readme is installed with the package
* [5cd7aa5](https://github.com/halkeye/flask_atlassian_connect/commit/5cd7aa5) use default container based images
* [789f9ea](https://github.com/halkeye/flask_atlassian_connect/commit/789f9ea) pandoc
* [b66dbcd](https://github.com/halkeye/flask_atlassian_connect/commit/b66dbcd) build build build
* [04218f4](https://github.com/halkeye/flask_atlassian_connect/commit/04218f4) "python setup.py test" works now
* [4999de7](https://github.com/halkeye/flask_atlassian_connect/commit/4999de7) init

## [0.0.2](https://github.com/halkeye/flask_atlassian_connect/compare/0.0.1...0.0.2)

* [b850fe3](https://github.com/halkeye/flask_atlassian_connect/commit/b850fe3) fix up docs
* [1dc0cf2](https://github.com/halkeye/flask_atlassian_connect/commit/1dc0cf2) delete/all/save/load of Client
* [f04425a](https://github.com/halkeye/flask_atlassian_connect/commit/f04425a) feat: add tasks() function that will return a pyinvoke collection
* [d38974d](https://github.com/halkeye/flask_atlassian_connect/commit/d38974d) fix: App is not necessarily defined at creation, move full link creation to when desciptor is being outputted
* [7d327eb](https://github.com/halkeye/flask_atlassian_connect/commit/7d327eb) slight docs cleanup
* [5e8dbcc](https://github.com/halkeye/flask_atlassian_connect/commit/5e8dbcc) Feat: add atlassian_jwt_post_url template variable to code/docs
* [05aa955](https://github.com/halkeye/flask_atlassian_connect/commit/05aa955) Rename Client to AtlassianConnectClient
* [36dffe8](https://github.com/halkeye/flask_atlassian_connect/commit/36dffe8) fix flake8 warning
* [df0c584](https://github.com/halkeye/flask_atlassian_connect/commit/df0c584) fix: Handle functions returning strings or templates, and only default if nothing is provided
* [c6d8248](https://github.com/halkeye/flask_atlassian_connect/commit/c6d8248) Add some simple configuration. Clean it up later
* [5d050d7](https://github.com/halkeye/flask_atlassian_connect/commit/5d050d7) move the .nojekyll support to sphix so its a little cleaner
* [ca6c30a](https://github.com/halkeye/flask_atlassian_connect/commit/ca6c30a) add .nojekyll
* [c05c8ff](https://github.com/halkeye/flask_atlassian_connect/commit/c05c8ff) Ahhh, GH_TOKEN should be an env variable, and referenced in the deploy
* [4876e00](https://github.com/halkeye/flask_atlassian_connect/commit/4876e00) deploy docs to gh-pages
* [2991fd6](https://github.com/halkeye/flask_atlassian_connect/commit/2991fd6) meh commit to re trigger travis
* [b98b9e9](https://github.com/halkeye/flask_atlassian_connect/commit/b98b9e9) install sphix stuff after everything else is tested so it can't mess with things
* [9daa450](https://github.com/halkeye/flask_atlassian_connect/commit/9daa450) webpanel documentation
* [ad59663](https://github.com/halkeye/flask_atlassian_connect/commit/ad59663) docs: flesh out the lifecycle docs a bit more
* [4143191](https://github.com/halkeye/flask_atlassian_connect/commit/4143191) docs: Adding webhook and module decorator docs
* [5d524f2](https://github.com/halkeye/flask_atlassian_connect/commit/5d524f2) don't double test on travis
* [3ca4b9b](https://github.com/halkeye/flask_atlassian_connect/commit/3ca4b9b) docs: fix a little bit of earlier copy and pate
* [c77e3c2](https://github.com/halkeye/flask_atlassian_connect/commit/c77e3c2) add some more webhooks documentation
* [5fa170e](https://github.com/halkeye/flask_atlassian_connect/commit/5fa170e) docs: remove rogue import from docs
* [7823ce2](https://github.com/halkeye/flask_atlassian_connect/commit/7823ce2) lets try deploying docs after a build
* [e3142fb](https://github.com/halkeye/flask_atlassian_connect/commit/e3142fb) Logo support for documentation
* [9a28e68](https://github.com/halkeye/flask_atlassian_connect/commit/9a28e68) I like these docs now
* [14137cc](https://github.com/halkeye/flask_atlassian_connect/commit/14137cc) 3.6 is hard, later later later
* [3c75cff](https://github.com/halkeye/flask_atlassian_connect/commit/3c75cff) remove print statement so python 3 can run again. and its not needed
* [957ce1b](https://github.com/halkeye/flask_atlassian_connect/commit/957ce1b) test in python 3 too
* [5784c55](https://github.com/halkeye/flask_atlassian_connect/commit/5784c55) remove old pandoc stuff
* [3a78968](https://github.com/halkeye/flask_atlassian_connect/commit/3a78968) Fix that encryption, was pointed at the wrong travis repo
* [284565e](https://github.com/halkeye/flask_atlassian_connect/commit/284565e) remove some extra whitespace
* [ff7371a](https://github.com/halkeye/flask_atlassian_connect/commit/ff7371a) make setup.py great again
* [422ec08](https://github.com/halkeye/flask_atlassian_connect/commit/422ec08) fix a couple warnings
* [f23732e](https://github.com/halkeye/flask_atlassian_connect/commit/f23732e) Starting documentation
* [39dc6b8](https://github.com/halkeye/flask_atlassian_connect/commit/39dc6b8) Clean up reference client class so its a bit more useful
* [b94eaaa](https://github.com/halkeye/flask_atlassian_connect/commit/b94eaaa) cleanup
* [36b8b79](https://github.com/halkeye/flask_atlassian_connect/commit/36b8b79) rewrite based on what i've learned over the last couple of weeks. Should mostly comply to pypi standards now
* [f5f8964](https://github.com/halkeye/flask_atlassian_connect/commit/f5f8964) fix: make sure to return the actual webhook function so it can still be manually called
* [7c1b8dd](https://github.com/halkeye/flask_atlassian_connect/commit/7c1b8dd) feat: handle events routing for you. decorator will just do event handling
* [69f9f92](https://github.com/halkeye/flask_atlassian_connect/commit/69f9f92) skip cleanup on travis for deploys
* [b7cb11b](https://github.com/halkeye/flask_atlassian_connect/commit/b7cb11b) 0.0.2
* [21e8c77](https://github.com/halkeye/flask_atlassian_connect/commit/21e8c77) refactor: attempt to reduce the amount of duplicated code in tests
* [5e909c6](https://github.com/halkeye/flask_atlassian_connect/commit/5e909c6) feat: basic module decorator test
* [f2e6d69](https://github.com/halkeye/flask_atlassian_connect/commit/f2e6d69) feat: Tests for webpanel
* [811dd57](https://github.com/halkeye/flask_atlassian_connect/commit/811dd57) refactor: Replace the descriptor with direct functions to make pylint stop whining
* [4866785](https://github.com/halkeye/flask_atlassian_connect/commit/4866785) Figured out why i suddenly had a lot of debug messages, remove global debugging logic
* [59e44d0](https://github.com/halkeye/flask_atlassian_connect/commit/59e44d0) more codacy
* [46e07a4](https://github.com/halkeye/flask_atlassian_connect/commit/46e07a4) ci: codacy code coverage util
* [ad82aa4](https://github.com/halkeye/flask_atlassian_connect/commit/ad82aa4) refactor: Fix up minor issues reported by codacy
* [904cbbc](https://github.com/halkeye/flask_atlassian_connect/commit/904cbbc) remove trailing space
* [0847697](https://github.com/halkeye/flask_atlassian_connect/commit/0847697) fix: python setup.py tests will now run the right directory
* [df27ae2](https://github.com/halkeye/flask_atlassian_connect/commit/df27ae2) fix: tell setuptools to autofind packages after i forgot to fix it after the last refactor
* [8a13423](https://github.com/halkeye/flask_atlassian_connect/commit/8a13423) feat: basic webhook support
* [c32eb7e](https://github.com/halkeye/flask_atlassian_connect/commit/c32eb7e) feat: support overring list of scopes
* [e1f9614](https://github.com/halkeye/flask_atlassian_connect/commit/e1f9614) ci: RAWR. try having no specific requirements for version
* [2ff1886](https://github.com/halkeye/flask_atlassian_connect/commit/2ff1886) ci: RAWR. try having no specific requirements for version
* [e276722](https://github.com/halkeye/flask_atlassian_connect/commit/e276722) ci: RAWR. try having no specific requirements for version
* [619bc33](https://github.com/halkeye/flask_atlassian_connect/commit/619bc33) fix: version conflict for mock
* [463b53a](https://github.com/halkeye/flask_atlassian_connect/commit/463b53a) ci: donno why this is working locally and not in travis
* [54fc104](https://github.com/halkeye/flask_atlassian_connect/commit/54fc104) ci: upgrade pip, remove pandoc
* [265ee6f](https://github.com/halkeye/flask_atlassian_connect/commit/265ee6f) ci: donno why this is working locally and not in travis
* [d6cc7f8](https://github.com/halkeye/flask_atlassian_connect/commit/d6cc7f8) fix: make sure all testing requirements are installed when running tests
* [693aaf2](https://github.com/halkeye/flask_atlassian_connect/commit/693aaf2) ci: Tell travis to run tests
* [9ade918](https://github.com/halkeye/flask_atlassian_connect/commit/9ade918) fix: dependancies should be set to minimum version
* [55c7d39](https://github.com/halkeye/flask_atlassian_connect/commit/55c7d39) fix: require the new 1.8.1 version of atlassian_jwt
* [e004f63](https://github.com/halkeye/flask_atlassian_connect/commit/e004f63) cleanup based on other modules i've found online
* [9b90c26](https://github.com/halkeye/flask_atlassian_connect/commit/9b90c26) refactor: don't need mock and reqeusts and stuff except for running tests
* [c421779](https://github.com/halkeye/flask_atlassian_connect/commit/c421779) fix: fix name matching
* [e7f851f](https://github.com/halkeye/flask_atlassian_connect/commit/e7f851f) fix: Most of the type client is going to be an object not a dict
* [a779f27](https://github.com/halkeye/flask_atlassian_connect/commit/a779f27) cleanup based on other modules i've found online
* [1ff66d5](https://github.com/halkeye/flask_atlassian_connect/commit/1ff66d5) don't need mock and reqeusts and stuff except for running tests
* [a247c7c](https://github.com/halkeye/flask_atlassian_connect/commit/a247c7c) fix name matching
* [4458a2e](https://github.com/halkeye/flask_atlassian_connect/commit/4458a2e) Most of the type client is going to be an object not a dict
* [961a138](https://github.com/halkeye/flask_atlassian_connect/commit/961a138) shrug at this point
* [306834f](https://github.com/halkeye/flask_atlassian_connect/commit/306834f) Travis
* [5657e56](https://github.com/halkeye/flask_atlassian_connect/commit/5657e56) fix install
* [b318a8a](https://github.com/halkeye/flask_atlassian_connect/commit/b318a8a) fun times travis testing
* [57c30ee](https://github.com/halkeye/flask_atlassian_connect/commit/57c30ee) make sure readme is installed with the package
* [5cd7aa5](https://github.com/halkeye/flask_atlassian_connect/commit/5cd7aa5) use default container based images
* [789f9ea](https://github.com/halkeye/flask_atlassian_connect/commit/789f9ea) pandoc
* [b66dbcd](https://github.com/halkeye/flask_atlassian_connect/commit/b66dbcd) build build build
* [04218f4](https://github.com/halkeye/flask_atlassian_connect/commit/04218f4) "python setup.py test" works now
* [4999de7](https://github.com/halkeye/flask_atlassian_connect/commit/4999de7) init

