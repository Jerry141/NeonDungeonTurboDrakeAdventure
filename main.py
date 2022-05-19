#!/usr/bin/env python3
import traceback

import tcod

import color
import exceptions
import setup_game
import input_handlers


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    # If the current event handler has an active Engine then save it.
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game Saved!")


def main() -> None:
    # screen size
    screen_width = 80
    screen_height = 50

    # specify the tilest from dejavu10x10_gs_tc.png stored in img folder
    tileset = tcod.tileset.load_tilesheet(
        "img\dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    
    # creating the screen from defined tileset
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Neon Synthwave Dungeon", # TODO find better name
        vsync=True,
    ) as context:
        # creating console to write to
        # order="F" changes [y,x] to [x,y]
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        # initializing game loop
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise

if __name__ == "__main__":
    main()