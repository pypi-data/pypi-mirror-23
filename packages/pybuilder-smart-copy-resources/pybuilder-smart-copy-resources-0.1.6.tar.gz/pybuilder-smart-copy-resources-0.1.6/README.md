# PyBuilder SmartCopyResources plugin

[PyBuilder](http://pybuilder.github.io/) plugin for copying additional resources to various destinations, e.g. to a `dist` directory altogether with the package.

## How to use it

In your `build.py`:

```
use_plugin("pypi:pybuilder_smart_copy_resources")
```

Then you can use smart_copy_resources plugin as part of built-in `package` task.
You do not have to call `package` task directly if use any task which requires it, for example, `publish` task. 

To configure the additional resource files you want to copy, use the following in your `build.py`:

```
@init
def set_properties(project):
    project.set_property("smart_copy_resources_basedir", "./dist")
    project.set_property("smart_copy_resources", {
        "path/to/file.ext": "./",
        "all/files/here/*": "./other/files",
        "${name}-additional-files/*": "./additional-files",
    })
```

`smart_copy_resources_basedir` is a base directory where the resource files are searched for. Files defined as keys in the `smart_copy_resources` dictionary will be copied into the locations specified by corresponding values. The files can be specified as `glob` patterns. Sources and destinations may contain project properties placeholders, e.g. `${name}` or `${version}`.

You can also use the extended notation to alter the filenames:

```
    project.set_property("smart_copy_resources", {
        "path/to/file.ext": {
            "copy_as": "new_file.ext",
            "destination": ./dist,
        }
    })

```

Do **NOT** use `glob` patterns in this extended notation as all the files would be copied into the requested location with the new filename. Thus, only one file will be created in the destination in fact.


