angular.module('sandstone.filetreedirective', [])

.directive('sandstoneFiletree', [function(){
  return {
    restrict: 'A',
    scope: {
      extraOptions: '=options',
      extraOnSelect: '&onSelect',
      extraOnToggle: '&onToggle',
      treeData: '=',
      filterExpression: '=',
      filterComparator: '='
    },
    templateUrl: '/static/core/components/filetreedirective/templates/filetree.html',
    controller: ['$scope', '$element', '$rootScope', 'FilesystemService', 'AlertService', function($scope, $element, $rootScope, FilesystemService, AlertService) {
      var self = $scope;

      if (self.treeData.contents.length === 0) {
        var fsDetails = FilesystemService.getFilesystemDetails();
        fsDetails.then(
          function(filesystem) {
            for (var i=0;i<filesystem.volumes.length;i++) {
              filesystem.volumes[i].name = filesystem.volumes[i].filepath;
              self.treeData.contents.push(filesystem.volumes[i]);
            }
          },
          function(data, status) {
            AlertService.addAlert({
              type: 'danger',
              message: 'Failed to retrieve filetree contents. Please refresh this page.',
              close: false
            });
          }
        );
      }

      // Options
      self.options = {
        multiSelection: false,
        isLeaf: function(node) {
          return node.type === 'file';
        },
        injectClasses: {
          iExpanded: "filetree-icon fa fa-caret-down",
          iCollapsed: "filetree-icon fa fa-caret-right",
          iLeaf: "filetree-icon fa"
        }
      };

      self.$watch('extraOptions', function(newValue,oldValue) {
        if (self.extraOptions) {
          angular.extend(self.options,self.extraOptions);
        }
      }, true);

      // Tree contents
      self.isExpanded = function (filepath) {
        for (var i=0;i<self.treeData.expanded.length;i++) {
          if (self.treeData.expanded[i].filepath === filepath) {
            return true;
          }
        }
        return false;
      };

      self.onSelect = function(node,selected) {
        if (self.extraOnSelect) {
          self.extraOnSelect({node: node, selected: selected});
        }
      };

      var getChildrenForDirectory = function(node) {
        var dirChildren = {};
        if (node.children) {
          var children = node.children;
          for (var i=0;i<children.length;i++) {
            if (children[i].children && (children[i].children.length > 0)) {
              dirChildren[children[i].filepath] = children[i].children;
            }
          }
        }
        return dirChildren;
      };

      self.loadDirectoryContents = function(node) {
        var dirDetails = FilesystemService.getDirectoryDetails(node.filepath);
        dirDetails.then(
          function(directory) {
            var prevChildren = getChildrenForDirectory(node);
            var newChildren = [];
            for (var i=0;i<directory.contents.length;i++) {
              var dir = directory.contents[i];
              if (dir.filepath in prevChildren) {
                dir.children = prevChildren[dir.filepath];
              }
              newChildren.push(dir);
            }
            node.children = newChildren;
          },
          function(data, status) {
            AlertService.addAlert({
              type: 'warning',
              message: 'Failed to retrieve contents for ' + node.filepath
            });
          }
        );
      };

      self.updateDirectoryContents = function(filepath) {
        var node, nodeNormPath;
        var normPath = FilesystemService.normalize(filepath);
        for (var i=0;i<self.treeData.expanded.length;i++) {
          node = self.treeData.expanded[i];
          nodeNormPath = FilesystemService.normalize(node.filepath);
          if (nodeNormPath === normPath) {
            self.loadDirectoryContents(node);
            break;
          }
        }
      };

      $rootScope.$on('filesystem:file_created', function(event, data) {
        self.updateDirectoryContents(data.dirpath);
      });

      $rootScope.$on('filesystem:file_deleted', function(event, data) {
        self.updateDirectoryContents(data.dirpath);
      });

      $rootScope.$on('filesystem:file_moved', function(event, data) {
        self.updateDirectoryContents(data.src_dirpath);
        self.updateDirectoryContents(data.dest_dirpath);
      });

      self.onToggle = function(node,expanded) {
        var watcher;
        if (self.extraOnToggle) {
          self.extraOnToggle({node: node, expanded: expanded});
        }

        if (expanded) {
          self.loadDirectoryContents(node);
          watcher = FilesystemService.createFilewatcher(node.filepath);
        } else {
          watcher = FilesystemService.deleteFilewatcher(node.filepath);
        }

      };
    }
  ]};
}]);
