"""CLI entrypoint 'mutils' command"""

import click


@click.group()
@click.pass_context
def mutils(ctx, **kwargs):
    """CLI entrypoint and base command"""

    ctx.ensure_object(dict)
    ctx.obj.update(kwargs)
