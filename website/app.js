String.prototype.capitalize = function () {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

angular.module('patientPapers', [])
    .controller('PatientPapersController', function ($scope, $http) {
        var patientPapers = this

        var baseUrl = 'http://patientpapers.com:5000';

        $scope.disp = {
            'searchResults': false,
            'loadingSpinner': false,
            'errorBox': false,
            'headerBlock': true,
            'patientView': true
        }

        function resetDisplay() {
            $scope.disp = {
                'loadingSpinner': false,
                'errorBox': false,
                'headerBlock': true
            }
        }
        resetDisplay();

        $scope.$watch('search.q', function () {
            resetDisplay();
        });

        $scope.search = {
            q: ""
        };

        $scope.patientList = [];

        $scope.patient = {};

        function passOutSearchResult(patients) {
            $scope.patientList = [];
            for (i = 0; i < patients.length; i++) {
                var patient = patients[i];

                var gender = patient['gender'].capitalize();
                if (gender.toUpperCase() == 'MALE') {
                    gender += ' ♂';
                } else if (gender.toUpperCase() == 'FEMALE') {
                    gender += ' ♀';
                }

                var dead = false;
                if (patient['deceasedDateTime'] != undefined) {
                    dead = true;
                }
                var deathDate = "";
                if (dead) {
                    deathDate = patient['deceasedDateTime'].slice(0,10);
                }

                $scope.patientList.push({
                    'id': i,
                    'forename': patient['name'],
                    'surname': patient['surname'],
                    'name': patient['name'] + ' ' + patient['surname'],
                    'gender': gender,
                    'birthdate': patient['birthdate'],
                    'dead': dead,
                    'deathDate': deathDate
                })
            }
        }

        function getError() {
            $scope.disp['loadingSpinner'] = false;
            $scope.disp['searchResults'] = false;
            $scope.disp['errorBox'] = true;
            $scope.disp['headerBlock'] = false;
        }

        $scope.getPatient = function () {
            $scope.disp['loadingSpinner'] = true;
            $scope.disp['searchResults'] = false;
            $scope.disp['patientView'] = false;

            console.log('Searching for: ' + $scope.search.q)
            $http({
                method: 'GET',
                url: baseUrl + '/search',
                params: {
                    'q': $scope.search.q
                }
            }).then(function successCallback(response) {
                if (response.data.length > 0) {
                    $scope.disp['loadingSpinner'] = false;
                    $scope.disp['searchResults'] = true;
                    console.log(response);
                    passOutSearchResult(response.data);
                } else {
                    getError();
                }

            }, function errorCallback(response) {
                console.log(response);
                getError();

            });
        };

        $scope.loadPatient = function (id) {
            var patient = $scope.patientList[id];
            console.log(patient);
            $scope.disp['loadingSpinner'] = false;
            $scope.disp['searchResults'] = false;
            $scope.disp['errorBox'] = false;
            $scope.disp['headerBlock'] = true;

            $scope.patient = patient;
            $scope.disp['patientView'] = true;
        }
    });